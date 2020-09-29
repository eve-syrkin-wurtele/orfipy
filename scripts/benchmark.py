#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:43:24 2020

@author: usingh

Use this script to benchmark runtimes of different tools

arguments[1]<-input_fasta_file
"""

from pyrpipe import pyrpipe_engine as pe
import sys

N="5"
minlen="3"
outdir="times_out"
testseq=sys.argv[1]
#compare orfipy, orfm, getorf
orfipy_cmd=["bash", "run_orfipy.sh",testseq,outdir,minlen,N]
orfm_cmd=["bash", "run_orfm.sh",testseq,outdir,minlen,N]
getorf_cmd=["bash", "run_getorf.sh",testseq,outdir,minlen,N]
pe.execute_command(getorf_cmd,objectid="test",command_name="getorf")
pe.execute_command(orfipy_cmd,objectid="test",command_name="orfipy")
pe.execute_command(orfm_cmd,objectid="test",command_name="orfm")

#compare seqs
#python compare_fasta_files.py ../testdata/getorf_d ../testdata/orfm_d ../testdata/orfipy_testout/d
#python compare_fasta_files.py ../testdata/getorf_p ../testdata/orfm_p ../testdata/orfipy_testout/p


###Compare orfipy and getorf -3 option
orfipy_cmd=["bash", "run_orfipy_3.sh",testseq,outdir,minlen,N]
getorf_cmd=["bash", "run_getorf_3.sh",testseq,outdir,minlen,N]
pe.execute_command(getorf_cmd,objectid="test",command_name="getorf_3")
pe.execute_command(orfipy_cmd,objectid="test",command_name="orfipy_3")

###pyrpipe_diagnostic.py benchmark pyrpipe_logs/2020-09-29-16_31_25_pyrpipe.log