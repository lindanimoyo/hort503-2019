# Assignment 13 Answers

For this assignment we will be storing our compiled software in the directory `/data/hort503/$USER/software` and we will compile our software in this directory `/data/hort503/$USER/software/src`.

Inside of the `/data/hort503/$USER/software` directory we will create a folder for each software that includes it's name and version number (e.g. `hmmer-3.2.1`).

Let's set this up!  Move to my working directory and create the `src` folder where we will compile the code
```bash
cd /data/hort503/$USER
mkdir software
mkdir software/src
```

## Exercises Set 1
### Exercise 1.

> Follow the steps above to install the HMMER suite (from source) as well as muscle (from binaries) in your $HOME/local/bin directory. Ensure that you can run them from anywhere (including from your home directory) by running muscle --help and hmmsearch --help. Both commands should display help text instead of an error. Further, check that the versions being found by the shell are from your home directory by running which hmmsearch and which muscle.

*Note:* We will substitute for  `$HOME/local/bin` the paths we created above for software installation.


```

#### Install Hummer
Download and unpack Hummer
```bash
cd /data/hort503/$USER/software/src/
wget "http://eddylab.org/software/hmmer/hmmer-3.2.1.tar.gz" -O  hmmer-3.2.1.tar.gz
gzip -d hmmer-3.2.1.tar.gz
tar -xf hmmer-3.2.1.tar
```

Compile Hummer
```bash
cd hmmer-3.2.1
./configure --prefix=/data/hort503/$USER/software/hmmer-3.2.1
make
make install
```

#### Install Muscle

Download and unpack muscle
```bash
cd /data/hort503/$USER/software/src/
wget "http://www.drive5.com/muscle/downloads3.8.31/muscle3.8.31_i86linux64.tar.gz"
gzip -d muscle3.8.31_i86linux64.tar.gz
tar -xf muscle3.8.31_i86linux64.tar
```

Muscle is a binary, so we don't need to compile, it. Let's create a new folder for it and rename it so it's easier ot use.
```bash
cd /data/hort503/$USER/software
mkdir muscle-3.8.31
mv src/muscle3.8.31_i86linux64 ./muscle-3.8.31/muscle
```

### Exersice 2
> Determine whether you have the “NCBI Blast+” tools installed by searching for the blastn program. If they are installed, where are they located? If they are not installed, find them and install them from binaries.

Yes they are installed!
```bash
module avail blast
```
>-------------------------------------------------------- /data/ficklin/modulefiles >---------------------------------------------------------
>   blast/2.5.0    blast/2.8.1 (D)
>
>-------------------------------------------------------------- Other Software >--------------------------------------------------------------
>   blast/2.2.26    blast/2.7.1    rmblast/2.2.28    rmblast/2.6.0 (D)
>
>  Where:
>   D:  Default Module
>
>Use "module spider" to find all possible modules.
>Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

### Exercise 3
> Install sickle from the git repo at https://github.com/najoshi/sickle. To install it, you will need to follow the custom instructions inside of the README.md file. If you don’t have the git program, it is available for binary and source install at http://git-scm.com.

Download and unpack sickle:
```bash
cd /data/hort503/$USER/software/src
git clone https://github.com/najoshi/sickle.git
```
We don't want to use the development branch, let's use a specific release:

```bash
git checkout v1.33
```

Before we compile sickle we need to check the README which instructs us how to compile the software. It instructs us just to run `make`:

```bash
cd sickle
make
```

To install we can take the newly created binary named `sickle` and manually install it into our software directory:
```bash
cd /data/hort503/$USER/software
mkdir sickle-1.33
mv ./src/sickle/sickle ./sickle-1.33/sickle
```


## Exercises Set 2
### Exercise 1
> Create a new folder in your projects folder called c_elegans. Locate the FASTA file for the reference genome of Caenorhabditis elegans from http://wormbase.org, and download it to this folder using wget. The file you are searching for will be named something like c_elegans.PRJNA13758.WS244.genomic.fa.gz. After it is downloaded, decompress it and view it with less -S.

First create the project folder `c_elegans`
```bash
cd /data/hort503/$USER
mkdir c_elegans
cd c_elegans
```

Next, retrieve the files
```bash
wget ftp://ftp.flybase.net/releases/FB2019_02/dmel_r6.27/fasta/dmel-all-chromosome-r6.27.fasta.gz
gzip -d dmel-all-chromosome-r6.27.fasta.gz
```

### Exercise 2
> Install an SFTP client on your desktop, like FireFTP or CyberDuck, and attempt to connect to the same machine you log in to via SFTP. Download a FASTA file of some potentially homologous sequences from Uniprot to your local desktop, and transfer it to your remote c_elegans directory.

We did this in class on Tuesday! We installed [FileZilla](https://filezilla-project.org/)

For this you can download the same sequence as indicated in the tutorial:  `p450 1A1`.  I had to uncompress it after copying:

```bash
cd /data/hort503/$USER/c_elegans
gzip -d uniprot-p450+1a1-filtered-reviewed_yes.fasta.gz
```

### Exercise 3
> Try running muscle and HMMER on the sequences you downloaded from uniprot.org against the C. elegans genome.

First run `muscle` to perform the multiple sequence alignment between all of the p450 sequences we downloaded from Uniprot.
```bash
../software/muscle-3.8.31/muscle -in uniprot-p450+1a1-filtered-reviewed_yes.fasta -out p450s.fasta.aln
```

Second run `hmmbuild` to build a Hidden Markov Model (HMM) for the alignments.
```bash
../software/hmmer-3.2.1/bin/hmmbuild p450s.fasta.aln.hmm p450s.fasta.aln
```

Third run `hmmsearch` to find occurances of the
```bash
../software/hmmer-3.2.1/bin/hmmsearch p450s.fasta.aln.hmm dmel-all-chromosome-r6.27.fasta
```

### Exercise 4
> If you have access to more than one Unix-based machine (such as an OS X desktop and a remote Linux computer, or two remote Linux computers), read the man page for scp with man scp, and also read about it online. Try to transfer a file and a directory between machines using scp on the command line.

Transfering the same file as in Exercise #2 above but from my laptop (using MobaXterm on Windows or terminal on OSX or Linux)
```bash
scp uniprot-p450+1a1-filtered-reviewed_yes.fasta.gz stephen.ficklin@kamiak.wsu.edu:/data/hort503/stephen.ficklin/c_elegans

```

#### Exercise 5
> Write an executable bash script that automates a process of some kind, and install it in your $HOME/local/bin. Test it after logging out and back in.
