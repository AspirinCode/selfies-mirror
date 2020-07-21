# Changelog


---

## v0.2.4 - 01-10-2019:
### Added:
 *  Function ``get_alphabet()`` which returns a list of 29 selfies symbols
    whose arbitrary combination produce >99.99% valid molecules.
 
### Bug Fixes:
 *  Fixed bug which happens when three rings start at one node, and two of
    them form a double ring.
 *  Enabled rings with sizes of up to 8000 SELFIES symbols.
 *  Bug fix for tiny ring to RDKit syntax conversion, spanning multiple
    branches.

We thank Kevin Ryan (LeanAndMean@github), Theophile Gaudin and Andrew Brereton
for suggestions and bug reports.

---

## v0.2.2 - 19-09-2019:

### Added:
 *  Enabled ``[C@],[C@H],[C@@],[C@@H],[H]`` to use in a semantic
    constrained way.

We thank Andrew Brereton for suggestions and bug reports.

---

## v0.2.1 - 02-09-2019:

### Added:
 *  Decoder: added optional argument to restrict nitrogen to 3 bonds. 
    ``decoder(...,N_restrict=False)`` to allow for more bonds;
    standard: ``N_restrict=True``.
 *  Decoder: added optional argument make ring-function bi-local 
    (i.e. confirms bond number at target). 
    ``decoder(...,bilocal_ring_function=False)`` to not allow bi-local ring 
    function; standard: ``bilocal_ring_function=True``. The bi-local ring 
    function will allow validity of >99.99% of random molecules.
 *  Decoder: made double-bond ring RDKit syntax conform.
 *  Decoder: added state X5 and X6 for having five and six bonds free.
 
### Bug Fixes:
 * Decoder + Encoder: allowing for explicit brackets for organic atoms, for 
   instance ``[I]``.
 * Encoder: explicit single/double bond for non-canonical SMILES input
   issue fixed.
 * Decoder: bug fix for ``[Branch*]`` in state X1.

We thank Benjamin Sanchez-Lengeling, Theophile Gaudin and Zhenpeng Yao 
for suggestions and bug reports.

---

## v0.1.1 - 04-06-2019: 
 * initial release 
