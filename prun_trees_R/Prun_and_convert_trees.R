## Written by Nelson Buainain 2022

# install.packages('phytools')

# Load phytools
library("phytools")

# Set directory
setwd("./prun_trees_R/")

# List all files
files = list.files("../prun_trees_R/original_trees/","tree")

# Create output directory
dir.create("./pruned")

# Loop over files
for (f in 1:length(files)){
  
  # Read tree in nexus format
  tree <- read.nexus(paste0("./original_trees/",files[f]))
  
  # Or in tree format
  #tree <- read.tree("./tree_1.tre")
  
  # if your tree is not properly rooted, choose outgroup
  
  tree <- root(tree, "INPA_A19826_Atl_out", resolve.root=TRUE)
  
  # Unident the block below if you want to plot your tree and see how it looks like
  
  # par(fg="transparent")
  # cw<-reorder(tree,"cladewise")
  # plotTree(cw)
  # obj<-get("last_plot.phylo",envir=.PlotPhyloEnv)
  # par(fg="black")
  # text(rep(max(obj$xx[1:Ntip(cw)]),Ntip(cw)),obj$yy[1:Ntip(cw)],
  #      labels=cw$tip.label,font=2,pos=4,cex=0.5)
  # for(i in 1:Ntip(cw)) lines(c(obj$xx[i],max(obj$xx[1:Ntip(cw)])),
  #                            rep(obj$yy[i],2),lty="dotted")
  
  # Plot nodes if you would like to
  nodelabels(cex = .4, bg = "yellow")
  
  # Take a look at labels of tree tips
  tree$tip.label
  
  # Drop outgroup
  tree<-drop.tip(rooted_tree,"INPA_A19826_Atl_out")
  
  # Choose what samples you want to keep
  samples <- c("Andes_BT_800_Arr_aur_ery","ICN_35091_Arr_aur_occ","ANSP_189205_Arr_aur_aur",
         "USNM_607183_Arr_aur_ruf","LSU_33341_Arr_abe_nig",
         "LSU_66949_Arr_abe_abe","Andes_JEA01_Arr_sch_can",
         "IAvH_9621_Arr_sch_sch","Andes_O_432_Arr_tac_axi",
         "INPA_A19250_Arr_tac","LGEMA_1307_Arr_sem","MNT_394_Arr_fra",
         "ICN_39050_Arr_aur_spe","USNM_645466_Arr_dor","MFV_3908_Arr_fla",
         "MNT_4249_Arr_pol","FMNH_394031_Arr_bru_bru",
         "FMNH_393763_Arr_bru_ape","FMNH_393758_Arr_bru_kue_sut",
         "FMNH_346807_Arr_bru_sut","AMNH_DOT8471_Arr_vir_vir",
         "MVZ_188247_Arr_bru_mac","FMNH_481660_Arr_bru_all",
         "LSU_1371_Arr_bru_fro","LSU_26437_Arr_cra_cra",
         "FMNH_430070_Arr_cas_cas_se","ICN_37368_Arr_cra_eur",
         "AMNH_393016_Arr_cos","FMNH_430060_Arr_ass_pol",
         "ICN_38550_Arr_ass_ass","AMNH_DOT2507_Arr_tor_tor",
         "CU_55859_Arr_tor_bor","AMNH_520402_Arr_phy",
         "ICN_36474_Arr_bas","ICN_37349_Arr_ass_lar",
         "ICN_38244_Arr_per","ICN_35798_Arr_atr_atr")
  
  # Keep only one sample per taxa, drop the rest
  tree <- keep.tip(tree,samples)
  
  # Unident the block below if you want to plot your tree and see how it looks like
  
  # par(fg="transparent")
  # cw<-reorder(tree,"cladewise")
  # plotTree(cw)
  # obj<-get("last_plot.phylo",envir=.PlotPhyloEnv)
  # par(fg="black")
  # text(rep(max(obj$xx[1:Ntip(cw)]),Ntip(cw)),obj$yy[1:Ntip(cw)],
  #      labels=cw$tip.label,font=2,pos=4,cex=0.5)
  # for(i in 1:Ntip(cw)) {lines(c(obj$xx[i],max(obj$xx[1:Ntip(cw)])),
  #                            rep(obj$yy[i],2),lty="dotted")}
  
  write.nexus(tree, file = paste0("./pruned/",files[f]))
}

