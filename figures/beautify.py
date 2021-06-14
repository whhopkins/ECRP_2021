from ROOT import TFile, TCanvas, gROOT
import sys, ROOT
from setStyle import setStyle, CompLegend
gROOT.SetBatch()
setStyle()
inF = TFile.Open('TrackHistograms.root')
hist = inF.Get('volumes/EMEC/trackStepsWgt/EMEC_gamma_vol_trackStepsWgt')

c = TCanvas('c', '', 800, 600)
c.cd()
newHists = {}
for newNSteps in [2,5,10]:
    newHists[newNSteps] = hist.Clone()
    for binI in range(1, newHists[newNSteps].GetNbinsX()+1):
        if newHists[newNSteps].GetBinLowEdge(binI) > newNSteps:
            newHists[newNSteps].SetBinContent(binI, newHists[newNSteps].GetBinLowEdge(binI)*1./newNSteps)
        else:
             newHists[newNSteps].SetBinContent(binI,1)
hist.Scale(1./1000)
print "Percent of photons with more than 10 steps:", round(hist.Integral(10,hist.GetNbinsX())/hist.Integral()*100,1)
hist.SetTitle('')
hist.GetYaxis().SetTitle('Computational cost [arbritrary units]')
hist.GetXaxis().SetTitle('Number of steps')
hist.GetXaxis().SetRangeUser(0, 150)
titleSize=0.05
hist.GetXaxis().SetTitleSize(titleSize)
hist.GetYaxis().SetTitleSize(titleSize)
hist.GetYaxis().SetTitleOffset(1.1)
hist.Draw('hist')
c.Print('trackStepsWgt.pdf')

c.Clear()
firstHist = newHists[sorted(newHists.keys())[0]]
firstHist.SetLineColor(1)
firstHist.Draw('hist')

sortedHists = [firstHist]
lineColors = {1:1, 2:ROOT.kRed, 3:ROOT.kBlue, 4:ROOT.kMagenta, 5:ROOT.kGreen+2, 10:ROOT.kOrange}
for newNSteps in sorted(newHists.keys())[1:]:
    newHists[newNSteps].SetLineColor(lineColors[newNSteps])
    newHists[newNSteps].Draw('histsame')
    sortedHists.append(newHists[newNSteps])
    
firstHist.SetTitle('')
firstHist.GetYaxis().SetTitle('Improvement factor')
firstHist.GetXaxis().SetTitle('Number of steps')
firstHist.GetXaxis().SetRangeUser(0, 150)
titleSize=0.05
firstHist.GetXaxis().SetTitleSize(titleSize)
firstHist.GetYaxis().SetTitleSize(titleSize)
firstHist.GetYaxis().SetTitleOffset(1.1)
legTitles = ["Replacement steps = %d" % (newNSteps) for newNSteps in sorted(newHists.keys())]
leg = CompLegend((0.2, 0.4, 0.7, 0.9), sortedHists, legTitles)
leg.Draw('same')
c.Print('possibleImprovements.pdf')

# Now let's rescale the orignal plot with the improvement factor
c.Clear()
newCompCostHist = {1:hist.Clone()}
sortedHists = [newCompCostHist[1]]
newCompCostHist[1].Draw('hist')
for newNSteps in sorted(newHists.keys()):
    newCompCostHist[newNSteps]=hist.Clone()
    newCompCostHist[newNSteps].Divide(newHists[newNSteps])
    newCompCostHist[newNSteps].SetLineColor(lineColors[newNSteps])
    #newCompCostHist[newNSteps].Draw('histsame')
    sortedHists.append(newCompCostHist[newNSteps])
    print "Total computational improvement for replacement step %d: %d" % (newNSteps,round(newCompCostHist[newNSteps].Integral()/hist.Integral()*100))
newCompCostHist[5].SetFillColor(lineColors[5])
newCompCostHist[5].Draw('histsame')    
firstHist.SetTitle('')
firstHist.GetYaxis().SetTitle('Computational cost')
firstHist.GetXaxis().SetTitle('Number of steps')
firstHist.GetXaxis().SetRangeUser(0, 150)
titleSize=0.05
firstHist.GetXaxis().SetTitleSize(titleSize)
firstHist.GetYaxis().SetTitleSize(titleSize)
firstHist.GetYaxis().SetTitleOffset(1.1)
legTitles = ["No improvement", "Replacement steps = 5"]
#legTitles.extend(["Replacement steps = %d" % (newNSteps) for newNSteps in sorted(newCompCostHist.keys())[1:]])
leg = CompLegend((0.3, 0.6, 0.75, 0.9), [newCompCostHist[1], newCompCostHist[5]], legTitles)
leg.Draw('same')
c.Print('newCompCost.pdf')
