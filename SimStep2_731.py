# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --conditions auto:run2_mc -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW-HLTDEBUG -n 10 --magField 38T_PostLS1 --eventcontent FEVTDEBUGHLT --filein file:step1.root --fileout file:step2.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('HLT')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mix_CSA14_50ns_PoissonOOTPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_PostLS1_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
#process.load('HLTrigger.Configuration.HLT_GRun_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('hlt')

#pileup file
process.mix.input.fileNames = cms.untracked.vstring('/store/user/tucker/00131829-EF9F-E311-A211-80000048FE80.root')
#process.mix.input.fileNames = cms.untracked.vstring('/store/mc/Fall13/MinBias_TuneZ2star_13TeV_pythia6/GEN-SIM/POSTLS162_V1_castor-v4/00000/00131829-EF9F-E311-A211-80000048FE80.root')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
 #for running interactively
  'file:/eos/uscms/store/user/mzientek/Neutralino_M1TeV_13TeV_DisplaceVtx_GENSIM_721/Neutralino_M1TeV_13TeV_DisplaceVtx_GENSIM_721/9deefa5acb2c6fadfb6a8803bc643ebf/step1_8_1_xzK.root'
)
)

process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('step2 nevts:10'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(1048576),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    fileName = cms.untracked.string('file:step2_731_m900_ht6jet.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW-HLTDEBUG')
    )
)

# Additional output definition

# Other statements
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_GRun', '')
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgradePLS1','')

from CondCore.DBCommon.CondDBSetup_cfi import CondDBSetup
process.duh = cms.ESSource( "PoolDBESSource", CondDBSetup,
       connect = cms.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS" ),

 toGet = cms.VPSet(
     cms.PSet(  record = cms.string( "JetCorrectionsRecord" ),
       tag = cms.string( "JetCorrectorParametersCollection_HLT_V1_AK4Calo" ),
       connect = cms.untracked.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS" ),
       label = cms.untracked.string( "AK4CaloHLT" )
     ),
     cms.PSet(  record = cms.string( "JetCorrectionsRecord" ),
       tag = cms.string( "JetCorrectorParametersCollection_HLT_trk1B_V1_AK4PF" ),
       connect = cms.untracked.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS" ),
       label = cms.untracked.string( "AK4PFHLT" )
     )
   )
)

process.es_prefer_duh = cms.ESPrefer('PoolDBESSource', 'duh')


# Path and EndPath definitions
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("results_m900.root"),
    closeFileFast = cms.untracked.bool(True)
)

process.myEDAnalyzer = cms.EDAnalyzer('HtAnalyzer',
	htLabels = cms.VInputTag(
			cms.InputTag('hltPFHT4Jet'), 
		        cms.InputTag('hltPFHT5Jet'),
			cms.InputTag('hltPFHT6Jet'),
			cms.InputTag('hltPFHT7Jet'),
                        cms.InputTag('hltPFHT8Jet'),
                        cms.InputTag('hltPFHT9Jet'),
                        cms.InputTag('hltPFHT10Jet'),
                        cms.InputTag('hltPFHT11Jet'),
			cms.InputTag('hltPFHT12Jet')
  )
)

process.blah = cms.Path( process.HLTBeginSequence + process.hltL1sL1HTT150ORHTT175 + process.hltPrePFHT7504Jet + process.HLTAK4CaloJetsSequence + process.HLTAK4PFJetsSequence + process.hltPFHT4Jet + process.hltPFHT5Jet + process.hltPFHT6Jet + process.hltPFHT7Jet + process.hltPFHT8Jet + process.hltPFHT9Jet+ process.hltPFHT10Jet+ process.hltPFHT11Jet + process.hltPFHT12Jet + process.myEDAnalyzer + process.HLTEndSequence )

# Schedule definition
process.schedule = cms.Schedule(process.digitisation_step,process.L1simulation_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.blah])
process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.FEVTDEBUGHLToutput_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)




# End of customisation functions
