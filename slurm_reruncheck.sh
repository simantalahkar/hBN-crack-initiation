#!/bin/bash
#SBATCH --job-name=lmp_test
#SBATCH --partition=cpu
#SBATCH --mail-type=end
#SBATCH --mail-user=SIMANTALAHKAR@HOTMAIL.COM
#SBATCH --output=%j.out
#SBATCH --error=%j.err
#SBATCH -N 2
#SBATCH --ntasks-per-node=40

module purge
module load lammps/2020-cpu

ulimit -s unlimited
ulimit -l unlimited

INPUT=reruncheck.in

srun --mpi=pmi2 lmp -i $INPUT