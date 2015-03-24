#include "TH1F.h"
#include "TH1D.h"
#include "TH2F.h"
#include "TLorentzVector.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"

#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Common/interface/Handle.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/MET.h"


#include "HLTrigger/JetMET/interface/HLTHtMhtFilter.h"


#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/TrackReco/interface/Track.h"

#include <vector>
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "FWCore/Utilities/interface/InputTag.h"

 class HtAnalyzer : public edm::EDAnalyzer {
 public:
   explicit HtAnalyzer(const edm::ParameterSet&);
   void analyze(const edm::Event&, const edm::EventSetup&);


 private:
   const std::vector<edm::InputTag> htLabels_;
   const size_t num_;

   std::vector<TH1D*> h_ht;
   TH1D* h_pt;
   TH1D* h_eta;
   TH1D* h_sumpt;
   TH1D* histo;
   TH1D* h_et_leading;
   TH1D* h_njets;
   TH2D* h_et_njets;
};


HtAnalyzer::HtAnalyzer(const edm::ParameterSet& cfg) : 
   htLabels_ (cfg.getParameter<std::vector<edm::InputTag> >("htLabels") ),
   num_	     ( htLabels_.size() ) 
{

edm::Service<TFileService> fs;

  //char histoname;
  for (unsigned int i=0; i<num_; ++i) {
      //sprintf(histoname,"h_ht_%i",i); 
      histo = fs->make<TH1D>(TString::Format("h_ht_%i",i), "", 100, 0, 1000);
      h_ht.push_back(histo);
  }

  h_pt = fs->make<TH1D>("h_pt","", 200, 0, 1000);
  h_eta = fs->make<TH1D>("h_eta","", 100,-3.5,3.5);
  h_sumpt = fs->make<TH1D>("h_spt","", 200, 0, 1000);
  h_njets = fs->make<TH1D>("h_njets","",30,0,30);
  h_et_leading = fs->make<TH1D>("h_et_lead","",400,0,2000);
  h_et_njets = fs->make<TH2D>("h_et_njets","",400,0,2000,30,0,30);
}


void HtAnalyzer::analyze(const edm::Event& event, const edm::EventSetup& setup) {
  using namespace std;
  using namespace edm;
  using namespace reco;

  double spt = 0;
  double setx = 0;
  double sety = 0;
  double set = 0;
  int n = 0;
  int njets = 0;
 
  edm::Handle<reco::JetView> jets;
  event.getByLabel( edm::InputTag( "hltAK4PFJetsCorrected" ), jets); 
  if (jets->size() > 0){
     std::cout<< "Number of Jets = " << jets->size() << std::endl;
     for (reco::JetView::const_iterator j=jets->begin(); j!= jets->end(); ++j){
        n += 1;
        double pt = j->pt();
        double eta = j->eta();
        double phi = j->phi();
        double et = j->et();

        double px = et*cos(phi);
        double py = et*sin(phi);

        if ( et >= 40 && fabs(eta) <= 3 ){
          njets += 1;
          spt += et;
          h_et_leading->Fill(et);
          std::cout<< "n="<<n<<" pt="<<pt<< "et="<<px<<" "<<py<<" eta="<<eta<<" Ht* ="<<spt<<" Et ="<<setx<<" "<<sety<<std::endl;
        }
        if ( et >= 40 && fabs(eta) <= 3 ) {
          setx -= px;
          sety -= py;
          std::cout<< "n="<<n<<" pt="<<pt<<" et="<<px<<" "<<py<<" eta="<<eta<<" Ht ="<<spt<<" Et* ="<<setx<<" "<<sety<<std::endl;
        }
        else std::cout<<"n="<<n<<" pt="<<pt<<" et="<<px<<" "<<py<<" eta="<<eta<<" Ht ="<<spt<<" Et ="<<setx<<" "<<sety<<std::endl;

        h_pt->Fill(pt);
        h_eta->Fill(eta);
     }
     set = sqrt(setx*setx + sety*sety);
     std::cout<<"Ht1 = "<<spt<<std::endl;
     std::cout<<"Ht2 = "<<set<<std::endl;
     h_et_njets->Fill(spt,njets);
     h_njets->Fill(njets);
     h_sumpt->Fill(spt);
  }
   


  for (unsigned int i=0; i<num_; ++i) {
     edm::Handle<reco::METCollection> hht;
     event.getByLabel(htLabels_[i], hht);
     h_ht[i]->Fill((hht->size() > 0 )? hht->at(0).sumEt() : -1);
     std::cout<< i << " " << hht->at(0).sumEt()<< std::endl;
  }  


}

DEFINE_FWK_MODULE(HtAnalyzer);
