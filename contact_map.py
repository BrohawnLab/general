from distutils.command.build_scripts import first_line_re
import urllib.request
import Bio.PDB
import numpy as np
from datetime import datetime
import pylab

# references used to fix bugs and adapt code
"ref: https://www.tutorialspoint.com/biopython/biopython_quick_guide.htm"
"ref: https://warwick.ac.uk/fac/sci/moac/people/students/peter_cock/python/protein_contact_map/"

startTime = datetime.now()

# downloading pdb file
urllib.request.urlretrieve('https://files.rcsb.org/view/7SFK.pdb', '7SFK.pdb')
pdb_code = "7SFK"
pdb_filename = "7SFK.pdb"

structure = Bio.PDB.PDBParser(PERMISSIVE = True, QUIET = True).get_structure(pdb_code, pdb_filename)
model = structure[0]

# make a function that returns the distance between reside 1 and 2
def calc_residue_dist(residue_A, residue_B):
    diff_vector  = residue_A["CA"].coord - residue_B["CA"].coord
    distance = np.sqrt(np.sum(diff_vector * diff_vector))
    return distance

# calculate the distance matrix
def calc_dist_matrix(chain_one, chain_two) :
     answer = np.zeros((len(chain_one), len(chain_two)), np.float64)
     for row, residue_A in enumerate(chain_one):
         try:
            for col, residue_B in enumerate(chain_two):
                try:
                    answer[row, col] = calc_residue_dist(residue_A, residue_B)
                except KeyError:
                    break
         except KeyError:
             break
     print(answer)
     return answer 
 
dist_matrix = calc_dist_matrix(model["A"], model["A"])
contact_map = dist_matrix < 8
 
print ("Minimum distance", np.min(dist_matrix))
print ("Maximum distance", np.max(dist_matrix))

# plotting the distance matrix
pylab.matshow(np.transpose(dist_matrix))
pylab.colorbar()
pylab.show()
 
# plotting contact map
pylab.imshow(np.transpose(contact_map))
pylab.show()
