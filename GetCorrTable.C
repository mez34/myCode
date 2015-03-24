#include <iostream>
#include <fstream>
#include "TROOT.h"
#include "TStyle.h"
#include "TFile.h"
#include "TCanvas.h"
#include "TH2F.h"
#include "TH2D.h"
#include "TString.h"
#include "TLegend.h"
#include "TPaveStats.h"
#include "Math.h"

////////////////////////////////////
////////////////////////////////////
////////////////////////////////////

using namespace std;

ofstream TextOutFile("Correlations_m400Sel_ht6jet.txt");

void GetCorrTable(){
  TString in_file = "histos_m400_ht6jet.root";
  TString in_mass = "400";

  if (TextOutFile.is_open()){
     TextOutFile << "Correlation between Triggers\n";
     TextOutFile << "1st Trigger ---- 2nd Trigger ------- correlation\n";
  }

  getCorr(in_file,in_mass);

}

void getCorr(const TString input_file, const TString mass){
  gROOT->SetBatch(1);

  // load histograms
  TFile *file = new TFile(input_file);
  TH2F *num = (TH2F*)file->Get("SimpleTriggerEfficiency/triggers2d_pass_num");
  TH2F *den = (TH2F*)file->Get("SimpleTriggerEfficiency/triggers2d_pass_den");
  int npaths = num->GetNbinsX();
  npaths += 1;
  //std::cout<< npaths << " " << num->GetNbinsY()<< std::endl;

  // create 2D correlation histogram by dividing num/den
  TH2F *histo = new TH2F("histo","Correlation Between Triggers for M="+mass+"GeV",npaths,0,npaths,npaths,0,npaths);
  //histo = num->Divide(den);

  double value_num, value_den, correlation;
  string bin_x, bin_y;
  // loop over i for x and j for y
  for (int i=0; i<npaths; ++i){ 
    for (int j=0; j<npaths; ++j){
	bin_x = num->GetXaxis()->GetBinLabel(i);
	bin_y = num->GetYaxis()->GetBinLabel(j);
        value_num = num->GetBinContent(i,j);
        value_den = den->GetBinContent(i,j);
	if (value_den!=0){
	  correlation = value_num/value_den;
	}
	else{
	  correlation = 0;
	}
 	histo->Fill(i,j,correlation);
	if (i > j){
	  TextOutFile << bin_x <<" "<< bin_y<<" "<<correlation*100<<"% "<<value_num<<"/"<< value_den <<"\n";
	}
    }
  }  
 
  // create canvas for histograms
  TFile* rootfile = new TFile("CorrelationPlot_m"+mass+".root","RECREATE");
  rootfile->cd();

  // draw histogram on canvas
  histo->SetTitle("Correlation between Triggers for M = "+mass+" GeV"); 
  histo->Write();
  rootfile->Close();


}



