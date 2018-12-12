
########################################################
# Revision History
########################################################

########################################################
# Function High Lights
########################################################
# Regress list file supports recursive include format (use -f)
# The command line in regression file can be used to trigger single test case simulation
# The directory structure supports create tarball for single test case
# Directory structure supports multiple configuration (Macro define)
# Generating rerun command for each failed test cases
# Genrate regression list for failed test cases (Merge test cases if two cases are idential)


########################################################
# HELP
########################################################
# Option            Defalt    Description
# -h|help           off       Print help information. <CMD>
# -v|verbose        off       Dump executing info on STD (for debug). <CMD>
# -s|seed <N/rand>  0         Simulation seed
# -r|runone <S>     ''        Run single test case in regress file. 
# -int              off       Run single test case in interactive mode. <CMD>
# -t|tag <S>        ''        Tag for this simulation dump. <CMD>
# -cov              ''        Generate coverage after simulation.
# -name <S>         ''        Name of test case <REGF>.
# -nocomp           off       Skip compiling the design. <CMD>
# -norun            off       Skip running the simulation. <CMD>
# -reg|regress <F>  ''        Regression file <CMD>
# -max <N>          30        Run <N> test cases in parallel. (Default: 30)
# -prebuild <S>     ''        <S> is the path of shell script for prebuild phase
# -postbuild <S>    ''        <S> is the path of shell script for postbuild phase
# -prerun <S>       ''        <S> is the path of shell script for prerun phase
# -postrun <S>      ''        <S> is the path of shell script for postrun phase   
# -postreg <S>      ''        <S> is the path of shell script for postreg phase   
# -simfail <S>      ''        <S> is the path of shell script for simfail phase   
# -okerr <F>        ''        <F> is the path of file for describe OK errors.
# -okcase
# -do <F>           ''        <F> is the do file for MTI.
# -rmdir            on        Remove output files before running simulation
# -buildopt         ''        Build option for the simulator.
# -runopt           ''        Run option for the simulator.
# -email            ''        Send email to users when simulation finishes.
# -cleanpass        off       Remove simulation output files if test passes.
# -repeat <N>       1         Run the testcase for N times(usually with different seeds)
# -srclist <F>      ''        <F> is the source list file.
# -work <S>         ''        <S> is the work directory
# -comopt       # Common options
#
# Timeout value for all compilation
# Timeout value for single compilation
# Timeout value for single simulation
# Timeout value for all Simulation

########################################################
# Use Case
########################################################
# 
# 
# 

########################################################
# Classes
########################################################
# cLog      - 
# cFile     - 
# cPath     - 
# cFileop   - 
# cComp     - 
# cTest     - 
# cRegr     - 
# cRunsim   - 
# cUge      - SGE operations
#

class cLog:
  def __init__(self,name):
  def flush(self):
  def preexit(self):
  def info(self,msg):
  def error(self,msg):
  def fatal(self,msg):


class cFile:
  def __init__(self,name):
  def flush(self,fname):
  def mkdir(self,dname):
  def rmdir(self,dname):
  def remove(self,fname):
  def write(self,fname,msg):
  def append(self,fname,msg):
  def read(self,fname):
  def exists(self,fname):


class cPath:
  def 


class cUge:
  def __init__(self,name):
  def submit(self,exef):
  def execute(self,exef):
  def isActive(self,jid):
  def waitActive(self,jid):
  def waitInactive(self,jid):
  def kill(self,jid):
  def isKilled(self,jid):


