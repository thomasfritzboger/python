import numpy as np
array_2D = np.arange(1,17,1).reshape(4,4) 
print("My 2D array")
print(array_2D)
print("\n")

#Sum
print("Hvis man vil lægge tal sammen fra en række eller kollone axis 0/Y eller 1/X")
print("\n")
print("np.sum(array_2D, axis=0) Y-aksen")
print(np.sum(array_2D, axis=0))
print("\n")
print("np.sum(array_2D, axis=1) X-aksen")
print(np.sum(array_2D, axis=1))
print("\n\n")

array_3D = np.arange(1,19,1).reshape(3,2,3)
print("Eksempel med 3D array")
print(array_3D)
print("\n")
print("Sum på 0-aksen hvilket er Z, da man starter med den højeste akse, her regnes sum 1,7,13 osv")
print("np.sum(array_3D, axis=0) Z-aksen")
print(np.sum(array_3D, axis=0)) #3.akse eller z-aksen

# gennemsnit
print("\n\n")

print("Vores 2D array")
print(array_2D)
print("\n")
print("Gennemsnit af tal i X-aksen (1,2,3,4)")
print("np.mean(array_2D, axis=1) ")
print(np.mean(array_2D, axis=1))

print("\n\n")
# Max og min værdi
print("Find max værdi i x akse (rækkerne)")
print("np.max(array_2D, axis=1)")
print(np.max(array_2D, axis=1))

print("\n\n")
#udføre aritmetiske operation på alle tal i et ndarray
print("udføre aritmetiske operation på alle tal i et ndarray, her ganges alle tal med 2")
print("array_2D*2")
print("\n")
print(array_2D*2)

print("\n\n")
#Broadcasting
print("Broadcasting er når et mindre array bliver udvidet til samme størrelse som et større array, så man kan udføre ")
print("enkeltvise operationer på alle elementer, størrelserne af arrays skal være kompatible")
print("\n")
print("big array:")
array_big = np.arange(1,7,1).reshape(2,3)

array_small = np.arange(2,8,2)
print(array_big)
print("\n")
print("small array:")
print(array_small)
print("\n")
print("Resultat af at gange det store array med det lille:")
print("array_big*array_small")
print("\n")
print(array_big*array_small)

print("\n")
print("Det man skal forsetile sig er at det lille array udvides:")
print("[[2 4 6]")
print(" [2 4 6]]")
print("og man derefter udfører operationen for hvert element")
print("\n")
print("\n")