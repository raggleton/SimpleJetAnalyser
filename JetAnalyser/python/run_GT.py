"""
This config is for running with JEC in a GlobalTag.
This is to give a reference for each set of JEC.

74X_mcRun2_asymptotic_v5 :  Summer15_25nsV7
76X_mcRun2_asymptotic_RunIIFall15DR76_v1 : Fall15_25nsV2
"""

# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: py L1NtupleRECO -s RAW2DIGI --era=Run2_2016 --conditions=auto:run2_mc --filein=/store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat0to50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/20000/1E2B5203-7AAA-E511-B6FD-0CC47A4D762A.root --secondfilein=/store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/GEN-SIM-RAW/25nsFlat0to50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/20000/08F09D12-11AA-E511-9613-0025905A60D0.root --no_exec --no_output -n 200
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RAW2DIGI',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/AODSIM/25nsFlat0to50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/20000/1E2B5203-7AAA-E511-B6FD-0CC47A4D762A.root'),
    # secondaryFileNames = cms.untracked.vstring('/store/mc/RunIIFall15DR76/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/GEN-SIM-RAW/25nsFlat0to50NzshcalRaw_76X_mcRun2_asymptotic_v12-v1/20000/08F09D12-11AA-E511-9613-0025905A60D0.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('py nevts:200'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '74X_mcRun2_asymptotic_v5', '')  # Summer15_25nsV7
# process.GlobalTag = GlobalTag(process.GlobalTag, '76X_mcRun2_asymptotic_RunIIFall15DR76_v1', '')  # Fall15_25nsV2 JEC

process.jetAnalysis = cms.EDAnalyzer('JetAnalyser')

process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string('L1Ntuple_summer15V7_GT.root')
    # fileName = cms.string('L1Ntuple_fall15V2_GT.root')
)

# Path and EndPath definitions
process.load('JetMETCorrections.Configuration.JetCorrectors_cff')

process.p = cms.Path(process.ak4PFCHSL1FastL2L3CorrectorChain + process.jetAnalysis)
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule(process.p,process.endjob_step)
