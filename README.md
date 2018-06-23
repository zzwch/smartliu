## An in-house Command Line Interface to process tag-based scRNA-Seq data.

### Installation
`$cd path-to-smartliu`   
`$pip install --editable .`

or `$pip install `
### Prerequisite
1. some common genome analysis tools, Including but no limited to: `hisat2`, `samtools`, `htseq-count`, `bamtools`, `bam2fastx`, `R`,`multiqc`. see [tools] section in configs/mm10.config file to find more information.   

2. It is highly recommended to use `conda install your-tool-name` to install dependcies.   
If you are in China, try to use the local anaconda and bioconda mirrors. It will save your time very much.
```
$conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
$conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
$conda config --set show_channel_urls yes
$conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
```
`$conda install fastqc cutadapt hisat2 samtools htseq-count bam2fastx bamtools R perl multiqc`

3. genome and trancscriptome index files build by hisat2-build
### Usage    
use `smartliu --help` to see how to start    
eg.   
`smartliu -c mm10 -i raw_data -o smart_mm10 -p n_sample`
