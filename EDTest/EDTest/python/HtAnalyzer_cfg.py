import FWCore.ParameterSet.Config as cms

process = cms.Process("HtDemo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(


'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_10_1_sYJ.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_1_1_cYH.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_2_1_SBM.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_3_1_D4d.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_4_1_SIM.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_5_1_k82.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_6_1_PzZ.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_7_1_9cC.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_8_1_77d.root',
#'/store/user/mzientek/Neutralino_M400_13TeV_DisplaceVtx_GENSIM_721/Neutralino_731_m400_HLT_multijet/79d68df139174da000226880344c7406/step2_731_m400_multijet_9_1_BvS.root',
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("results.root"),
    closeFileFast = cms.untracked.bool(True)
)

process.myEDAnalyzer = cms.EDAnalyzer('HtAnalyzer',
	htLabels = cms.VInputTag(
			cms.InputTag('HLT_PFHT750_4Jet'), 
		        cms.InputTag('HLT_PFHT750_5Jet_v*'),
			cms.InputTag('HLT_PFHT750_6Jet_v*'),
			cms.InputTag('HLT_PFHT750_7Jet_v*'),
                        cms.InputTag('HLT_PFHT750_8Jet_v*'))
)
process.p = cms.Path(process.myEDAnalyzer) 




