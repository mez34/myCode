# myCode

~ WorkFlow ~
SimStep1,SimStep2,SimStep3,SimStep4 made by $ runTheMatrix.py -l 1306

MC Samples generated with SimStep1 and minSLHA.spc file that SPECIFIES NEUTRALINO WIDTH (needed for displaced vertices)
Below samples are made in CMSSW_7_2_1_patch2
Samples are published and locations are below and in Evernote in Note "13 TeV Neutralino mass sample datasets":

#400
/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/USER
#500
/Neutralino_M500_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M500_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/USER
#600
/Neutralino_M600_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M600_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/USER
#700
/Neutralino_M700_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M700_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/USER
#800
/Neutralino_M800_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M800_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/USER
#900
/Neutralino_M900_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M900_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/USER
#1000
/Neutralino_M1TeV_13TeV_DisplaceVtx_GENSIM_721/mzientek-Neutralino_M1TeV_13TeV_DisplaceVtx_GENSIM_721-9deefa5acb2c6fadfb6a8803bc643ebf/US

SimStep2_731.py   does DIGI, RAW, HLTDEBUG
 DEPENDS ON: 
  - hlt.py : the HLT menu MY VERSION is /dev/CMSSW_7_3_0/GRun/V47 (CMSSW_7_3_1_patch2_HLT3)
             with new paths for low HT, 6jet triggers
             called by:
             hltGetConfiguration /dev/CMSSW_7_3_0/GRun —-cff --offline --mc --unprescale --process TEST --globaltag auto:run2_mc_Grun > hlt.py

  CAN DO: simple_trigger_efficiency.py at this point on the SimStep2 output files to see efficiency of HLT alone. 
          GetCorrTable.C  makes a text file with the full correlation table from results of simple_trigger_efficiency.
          ** NEED TO SPECIFY TextOutFile, in_file, and in_mass .

SimStep3_731.py does RECO
miniAOD.py takes output RECO and does vertexing
Histos.py -- runs simple_trigger_efficiency on select triggers (those of interest) * see my version copied in this repository *
  ( use to look at efficiency for HLT after vertexing and ~8TeV analysis cuts. ) 
  GetCorrTable.C can be used to find the correlation table as before. 
  

