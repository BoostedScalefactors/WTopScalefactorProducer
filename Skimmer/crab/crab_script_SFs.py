#!/Usr-/bin/env python
import os,sys
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import * 

#this takes care of converting the input files from CRAB
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis

sys.path.append("../python")
from TTSkimmer import *

# NOTE : This file is configured to Process MC.
# If you want to process Data then ADD "jsonInput='Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt'"
# to the PostProcessor arguement below

p=PostProcessor(".", inputFiles(),                   # --> to submit with crab, use this
# p=PostProcessor(".", ["test_data_92X_NANO_10.root"], # --> for local tests, use this
                 "nFatJet>0&&FatJet_msoftdrop>30&&FatJet_pt>200&&MET_sumEt>40&& ( (nElectron > 0 && HLT_Ele115_CaloIdVT_GsfTrkIdT) || (nMuon > 0 && HLT_Mu50))" ,"keep_and_drop.txt",
                  modules=[TTbar_SemiLep()],provenance=False,fwkJobReport=False ,
                  haddFileName=  '94XXNanoV0-TTbar_SemiLep.root',jsonInput='Cert_294927-306462_13TeV_PromptReco_Collisions17_JSON.txt' )

p.run()

print "DONE"
