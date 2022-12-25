#!/usr/bin/env python
# coding: utf-8

# In[102]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as tck
import seaborn as sns


# In[2]:


os.chdir("/home/ministreliya/IB/hw_pandas_vis/")
os.listdir()


# In[3]:


get_ipython().system('unzip diffexpr_data.tsv.zip')


# # Task 1

# In[73]:


def read_gff(path_to_file):
    gff = pd.read_csv(path_to_file,
                      sep="\t",
                      header=0,
                      names=["chr", "source", "type", "start", "end", "score", "strand", "phase", "atributes"])
    return gff


def read_bed6(path_to_file):
    bed = pd.read_csv(path_to_file,
                      sep = "\t",
                      names = ["chr", "start", "end","name", "score", "strand"])
    return bed


# In[74]:


my_gff = read_gff("rrna_annotation.gff")
my_gff.head(4)


# In[75]:


my_bed = read_bed6("alignment.bed")
my_bed.head(4)


# In[76]:


my_gff["atributes"] = my_gff['atributes'].str[5:8].str.replace('_','')
my_gff.head(4)


# In[77]:


rRNA_num = my_gff[["chr", "atributes", "type"]].groupby(["chr", "atributes"]).count()
rRNA_num.reset_index(inplace = True)
rRNA_num.columns = ["Ref", "rRNA", "number"]
rRNA_num


# In[78]:


plt.subplots(figsize = (25, 15))

sns.barplot(data = rRNA_num,
            x = "Ref",
            hue = "rRNA",
            y = "number",
            palette = ["#DC143C", "#20B2AA", "#9400D3"])

plt.xticks(rotation = 90, size = 17)
plt.yticks(size = 17)

plt.xlabel("Reference Genome", fontsize = 25)
plt.ylabel("Number of rRNAs", fontsize = 25)

plt.legend(title = "rRNA type", title_fontsize = 25, loc = 2, fontsize=25)

plt.show()


# In[82]:


bed_intrsct = my_gff.merge(my_bed, on = "chr", suffixes = ('_gff', '_bed')).drop_duplicates()
bed_intrsct_rRNA = bed_intrsct.query('start_gff > start_bed & end_gff < end_bed')
bed_intrsct_rRNA


# # Task 2

# In[83]:


diff_exp = pd.read_csv('diffexpr_data.tsv', sep = '\t')
diff_exp


# In[94]:


sig_down = diff_exp.query("logFC < 0 & pval_corr < 0.05")
sig_up = diff_exp.query("logFC > 0 & pval_corr < 0.05")
nsig_down = diff_exp.query("logFC < 0 & pval_corr >= 0.05")
nsig_up = diff_exp.query("logFC > 0 & pval_corr >= 0.05")


# In[132]:


plt.rc("font", weight="bold")

plt.figure(figsize = (20, 12))

plt.scatter(x = sig_down["logFC"], y = sig_down["log_pval"], label = "Significantly downregulated", s = 30)
plt.scatter(x = sig_up["logFC"], y = sig_up["log_pval"], label = "Significantly upregulated", s = 30)
plt.scatter(x = nsig_down["logFC"], y = nsig_down["log_pval"], label = "Non-significantly downregulated", s = 30)
plt.scatter(x = nsig_up["logFC"], y = nsig_up["log_pval"], label = "Non-significantly downregulated", s = 30)

plt.axhline(-np.log10(0.05), linestyle = "--", color = "grey", lw = 2)
plt.text(7, 3, s = "p-value = 0.05", color = "grey", size = 15)
plt.axvline(0, linestyle = "--", color = "grey", lw = 2)

plt.legend(shadow=True, markerscale = 3, fontsize = 18)

plt.xlabel("log$_{2}$(fold change)", style = "italic", weight = "bold", size = 15)
plt.ylabel("-log$_{10}$(p value corrected)", style = "italic", weight = "bold", size = 15)

plt.tick_params(which = "major", size = 5)
plt.tick_params(which = "minor", size = 3)


plt.xlim([diff_exp["logFC"].min() - 1, diff_exp["logFC"].max() + 1])
plt.ylim([diff_exp["log_pval"].min() - 4, diff_exp["log_pval"].max() + 4])

plt.annotate(xy = (sig_down.sort_values(by = "logFC").iloc[0]["logFC"], sig_down.sort_values(by = "logFC").iloc[0]["log_pval"]),
             xytext = (sig_down.sort_values(by = "logFC").iloc[0]["logFC"] + 0.5, sig_down.sort_values(by = "logFC").iloc[0]["log_pval"] + 10), 
             text = sig_down.sort_values(by = "logFC").iloc[0]["Sample"],
             arrowprops = dict(facecolor = "red", shrink = 0.05),
             weight = "bold", size = 15)

plt.annotate(xy = (sig_down.sort_values(by = "logFC").iloc[1]["logFC"], sig_down.sort_values(by = "logFC").iloc[1]["log_pval"]),
             xytext = (sig_down.sort_values(by = "logFC").iloc[1]["logFC"] - 0.5, sig_down.sort_values(by = "logFC").iloc[1]["log_pval"] + 10), 
             text = sig_down.sort_values(by = "logFC").iloc[1]["Sample"],
             arrowprops = dict(facecolor = "red", shrink = 0.05),
             weight = "bold", size = 15)

plt.annotate(xy = (sig_up.sort_values(by = "logFC").iloc[-1]["logFC"], sig_up.sort_values(by = "logFC").iloc[-1]["log_pval"]),
             xytext = (sig_up.sort_values(by = "logFC").iloc[-1]["logFC"] + 0.5, sig_up.sort_values(by = "logFC").iloc[-1]["log_pval"] + 10), 
             text = sig_up.sort_values(by = "logFC").iloc[-1]["Sample"],
             arrowprops = dict(facecolor = "red", shrink = 0.05),
             weight = "bold", size = 15)

plt.annotate(xy = (sig_up.sort_values(by = "logFC").iloc[-2]["logFC"], sig_up.sort_values(by = "logFC").iloc[-2]["log_pval"]),
             xytext = (sig_up.sort_values(by = "logFC").iloc[-2]["logFC"] - 1, sig_up.sort_values(by = "logFC").iloc[-2]["log_pval"] + 10), 
             text = sig_up.sort_values(by = "logFC").iloc[-2]["Sample"],
             arrowprops = dict(facecolor = "red", shrink = 0.05),
             weight = "bold", size = 15)

plt.title("Volcano plot", style = "italic", weight = "bold", size = 35, pad = 30)

