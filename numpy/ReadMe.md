# Array creation routines

# Ones and Zeros

| 函数API                                                      | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`empty`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html#numpy.empty)(shape[, dtype, order]) | Return a new array of given shape and type, without initializing entries. |
| [`empty_like`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty_like.html#numpy.empty_like)(prototype[, dtype, order, subok]) | Return a new array with the same shape and type as a given array. |
| [`eye`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html#numpy.eye)(N[, M, k, dtype, order]) | Return a 2-D array with ones on the diagonal and zeros elsewhere. |
| [`identity`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.identity.html#numpy.identity)(n[, dtype]) | Return the identity array.                                   |
| [`ones`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html#numpy.ones)(shape[, dtype, order]) | Return a new array of given shape and type, filled with ones. |
| [`ones_like`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ones_like.html#numpy.ones_like)(a[, dtype, order, subok]) | Return an array of ones with the same shape and type as a given array. |
| [`zeros`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html#numpy.zeros)(shape[, dtype, order]) | Return a new array of given shape and type, filled with zeros. |
| [`zeros_like`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros_like.html#numpy.zeros_like)(a[, dtype, order, subok]) | Return an array of zeros with the same shape and type as a given array. |
| [`full`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.full.html#numpy.full)(shape, fill_value[, dtype, order]) | Return a new array of given shape and type, filled with *fill_value*. |
| [`full_like`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.full_like.html#numpy.full_like)(a, fill_value[, dtype, order, subok]) | Return a full array with the same shape and type as a given array. |



## From existing data

| 函数API                                                      | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html#numpy.array)(object[, dtype, copy, order, subok, ndmin]) | Create an array.                                             |
| [`asarray`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.asarray.html#numpy.asarray)(a[, dtype, order]) | Convert the input to an array.                               |
| [`asanyarray`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.asanyarray.html#numpy.asanyarray)(a[, dtype, order]) | Convert the input to an ndarray, but pass ndarray subclasses through. |
| [`ascontiguousarray`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ascontiguousarray.html#numpy.ascontiguousarray)(a[, dtype]) | Return a contiguous array in memory (C order).               |
| [`asmatrix`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.asmatrix.html#numpy.asmatrix)(data[, dtype]) | Interpret the input as a matrix.                             |
| [`copy`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.copy.html#numpy.copy)(a[, order]) | Return an array copy of the given object.                    |
| [`frombuffer`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.frombuffer.html#numpy.frombuffer)(buffer[, dtype, count, offset]) | Interpret a buffer as a 1-dimensional array.                 |
| [`fromfile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfile.html#numpy.fromfile)(file[, dtype, count, sep]) | Construct an array from data in a text or binary file.       |
| [`fromfunction`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromfunction.html#numpy.fromfunction)(function, shape, **kwargs) | Construct an array by executing a function over each coordinate. |
| [`fromiter`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromiter.html#numpy.fromiter)(iterable, dtype[, count]) | Create a new 1-dimensional array from an iterable object.    |
| [`fromstring`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromstring.html#numpy.fromstring)(string[, dtype, count, sep]) | A new 1-D array initialized from text data in a string.      |
| [`loadtxt`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html#numpy.loadtxt)(fname[, dtype, comments, delimiter, …]) | Load data from a text file.                                  |



## Numerical ranges

| 函数API                                                      | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`arange`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html#numpy.arange)([start,] stop[, step,][, dtype]) | Return evenly spaced values within a given interval.         |
| [`linspace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html#numpy.linspace)(start, stop[, num, endpoint, …]) | Return evenly spaced numbers over a specified interval.      |
| [`logspace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logspace.html#numpy.logspace)(start, stop[, num, endpoint, base, …]) | Return numbers spaced evenly on a log scale.                 |
| [`geomspace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.geomspace.html#numpy.geomspace)(start, stop[, num, endpoint, dtype]) | Return numbers spaced evenly on a log scale (a geometric progression). |
| [`meshgrid`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html#numpy.meshgrid)(*xi, **kwargs) | Return coordinate matrices from coordinate vectors.          |
| [`mgrid`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mgrid.html#numpy.mgrid) | *nd_grid* instance which returns a dense multi-dimensional “meshgrid”. |
| [`ogrid`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ogrid.html#numpy.ogrid) | *nd_grid* instance which returns an open multi-dimensional “meshgrid”. |



## The Matrix class

| 函数API                                                      | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`mat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mat.html#numpy.mat)(data[, dtype]) | Interpret the input as a matrix.                             |
| [`bmat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.bmat.html#numpy.bmat)(obj[, ldict, gdict]) | Build a matrix object from a string, nested sequence, or array. |



## Building matrices

| 方法                                                         | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`diag`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.diag.html#numpy.diag)(v[, k]) | Extract a diagonal or construct a diagonal array.            |
| [`diagflat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.diagflat.html#numpy.diagflat)(v[, k]) | Create a two-dimensional array with the flattened input as a diagonal. |
| [`tri`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tri.html#numpy.tri)(N[, M, k, dtype]) | An array with ones at and below the given diagonal and zeros elsewhere. |
| [`tril`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tril.html#numpy.tril)(m[, k]) | Lower triangle of an array.                                  |
| [`triu`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.triu.html#numpy.triu)(m[, k]) | Upper triangle of an array.                                  |
| [`vander`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vander.html#numpy.vander)(x[, N, increasing]) | Generate a Vandermonde matrix.                               |





# Array manipulation routines

## Basic operations

| 方法                                                         | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`copyto`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.copyto.html#numpy.copyto)(dst, src[, casting, where]) | Copies values from one array to another, broadcasting as necessary. |



## Changing array shape

| 方法                                                         | 功能                                                     |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [`reshape`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html#numpy.reshape)(a, newshape[, order]) | Gives a new shape to an array without changing its data. |
| [`ravel`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel.html#numpy.ravel)(a[, order]) | Return a contiguous flattened array.                     |
| [`ndarray.flat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flat.html#numpy.ndarray.flat) | A 1-D iterator over the array.                           |
| [`ndarray.flatten`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html#numpy.ndarray.flatten)([order]) | Return a copy of the array collapsed into one dimension. |



## Transpose-like operations

|                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`moveaxis`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.moveaxis.html#numpy.moveaxis)(a, source, destination) | Move axes of an array to new positions.                      |
| [`rollaxis`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.rollaxis.html#numpy.rollaxis)(a, axis[, start]) | Roll the specified axis backwards, until it lies in a given position. |
| [`swapaxes`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.swapaxes.html#numpy.swapaxes)(a, axis1, axis2) | Interchange two axes of an array.                            |
| [`ndarray.T`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.T.html#numpy.ndarray.T) | Same as self.transpose(), except that self is returned if self.ndim < 2. |
| [`transpose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.transpose.html#numpy.transpose)(a[, axes]) | Permute the dimensions of an array.                          |



## Joining arrays

| 方法                                                         | 用途                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [`concatenate`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html#numpy.concatenate)((a1, a2, …)[, axis, out]) | Join a sequence of arrays along an existing axis.       |
| [`stack`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.stack.html#numpy.stack)(arrays[, axis, out]) | Join a sequence of arrays along a new axis.             |
| [`column_stack`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.column_stack.html#numpy.column_stack)(tup) | Stack 1-D arrays as columns into a 2-D array.           |
| [`dstack`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dstack.html#numpy.dstack)(tup) | Stack arrays in sequence depth wise (along third axis). |
| [`hstack`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.hstack.html#numpy.hstack)(tup) | Stack arrays in sequence horizontally (column wise).    |
| [`vstack`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vstack.html#numpy.vstack)(tup) | Stack arrays in sequence vertically (row wise).         |
| [`block`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.block.html#numpy.block)(arrays) | Assemble an nd-array from nested lists of blocks.       |



## Splitting arrays

| 函数API                                                      | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`split`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.split.html#numpy.split)(ary, indices_or_sections[, axis]) | Split an array into multiple sub-arrays.                     |
| [`array_split`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_split.html#numpy.array_split)(ary, indices_or_sections[, axis]) | Split an array into multiple sub-arrays.                     |
| [`dsplit`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dsplit.html#numpy.dsplit)(ary, indices_or_sections) | Split array into multiple sub-arrays along the 3rd axis (depth). |
| [`hsplit`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.hsplit.html#numpy.hsplit)(ary, indices_or_sections) | Split an array into multiple sub-arrays horizontally (column-wise). |
| [`vsplit`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vsplit.html#numpy.vsplit)(ary, indices_or_sections) | Split an array into multiple sub-arrays vertically (row-wise) |



## Tiling arrays

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`tile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tile.html#numpy.tile)(A, reps) | Construct an array by repeating A the number of times given by reps. |
| [`repeat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.repeat.html#numpy.repeat)(a, repeats[, axis]) | Repeat elements of an array.                                 |



## Adding and removing elements

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`delete`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.delete.html#numpy.delete)(arr, obj[, axis]) | Return a new array with sub-arrays along an axis deleted.    |
| [`insert`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.insert.html#numpy.insert)(arr, obj, values[, axis]) | Insert values along the given axis before the given indices. |
| [`append`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.append.html#numpy.append)(arr, values[, axis]) | Append values to the end of an array.                        |
| [`resize`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.resize.html#numpy.resize)(a, new_shape) | Return a new array with the specified shape.                 |
| [`trim_zeros`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.trim_zeros.html#numpy.trim_zeros)(filt[, trim]) | Trim the leading and/or trailing zeros from a 1-D array or sequence. |
| [`unique`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.unique.html#numpy.unique)(ar[, return_index, return_inverse, …]) | Find the unique elements of an array.                        |



# Indexing routines

## Generating index arrays

| 函数API                                                      | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`c_`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.c_.html#numpy.c_) | Translates slice objects to concatenation along the second axis. |
| [`r_`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.r_.html#numpy.r_) | Translates slice objects to concatenation along the first axis. |
| [`s_`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.s_.html#numpy.s_) | A nicer way to build up index tuples for arrays.             |
| [`nonzero`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nonzero.html#numpy.nonzero)(a) | Return the indices of the elements that are non-zero.        |
| [`where`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html#numpy.where)(condition, [x, y]) | Return elements, either from *x* or *y*, depending on *condition*. |
| [`indices`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.indices.html#numpy.indices)(dimensions[, dtype]) | Return an array representing the indices of a grid.          |
| [`ix_`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ix_.html#numpy.ix_)(*args) | Construct an open mesh from multiple sequences.              |
| [`ogrid`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ogrid.html#numpy.ogrid) | *nd_grid* instance which returns an open multi-dimensional “meshgrid”. |
| [`ravel_multi_index`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ravel_multi_index.html#numpy.ravel_multi_index)(multi_index, dims[, mode, …]) | Converts a tuple of index arrays into an array of flat indices, applying boundary modes to the multi-index. |
| [`unravel_index`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.unravel_index.html#numpy.unravel_index)(indices, dims[, order]) | Converts a flat index or array of flat indices into a tuple of coordinate arrays. |
| [`diag_indices`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.diag_indices.html#numpy.diag_indices)(n[, ndim]) | Return the indices to access the main diagonal of an array.  |
| [`diag_indices_from`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.diag_indices_from.html#numpy.diag_indices_from)(arr) | Return the indices to access the main diagonal of an n-dimensional array. |
| [`mask_indices`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mask_indices.html#numpy.mask_indices)(n, mask_func[, k]) | Return the indices to access (n, n) arrays, given a masking function. |
| [`tril_indices`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tril_indices.html#numpy.tril_indices)(n[, k, m]) | Return the indices for the lower-triangle of an (n, m) array. |
| [`tril_indices_from`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tril_indices_from.html#numpy.tril_indices_from)(arr[, k]) | Return the indices for the lower-triangle of arr.            |
| [`triu_indices`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.triu_indices.html#numpy.triu_indices)(n[, k, m]) | Return the indices for the upper-triangle of an (n, m) array. |
| [`triu_indices_from`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.triu_indices_from.html#numpy.triu_indices_from)(arr[, k]) | Return the indices for the upper-triangle of arr.            |



# Input and output

## Numpy binary files(NPY,NPZ)

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`load`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.load.html#numpy.load)(file[, mmap_mode, allow_pickle, …]) | Load arrays or pickled objects from `.npy`, `.npz` or pickled files. |
| [`save`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.save.html#numpy.save)(file, arr[, allow_pickle, fix_imports]) | Save an array to a binary file in NumPy `.npy` format.       |
| [`savez`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.savez.html#numpy.savez)(file, *args, **kwds) | Save several arrays into a single file in uncompressed `.npz` format. |
| [`savez_compressed`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed)(file, *args, **kwds) | Save several arrays into a single file in compressed `.npz` format. |



## Text files

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`loadtxt`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html#numpy.loadtxt)(fname[, dtype, comments, delimiter, …]) | Load data from a text file.                                  |
| [`savetxt`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.savetxt.html#numpy.savetxt)(fname, X[, fmt, delimiter, newline, …]) | Save an array to a text file.                                |
| [`genfromtxt`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt)(fname[, dtype, comments, …]) | Load data from a text file, with missing values handled as specified. |
| [`fromregex`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromregex.html#numpy.fromregex)(file, regexp, dtype[, encoding]) | Construct an array from a text file, using regular expression parsing. |
| [`fromstring`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fromstring.html#numpy.fromstring)(string[, dtype, count, sep]) | A new 1-D array initialized from text data in a string.      |
| [`ndarray.tofile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile)(fid[, sep, format]) | Write array to a file as text or binary (default).           |
| [`ndarray.tolist`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.tolist.html#numpy.ndarray.tolist)() | Return the array as a (possibly nested) list.                |



# Linear algebra

## Matrix and vector products

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`dot`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html#numpy.dot)(a, b[, out]) | Dot product of two arrays.                                   |
| [`linalg.multi_dot`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.multi_dot.html#numpy.linalg.multi_dot)(arrays) | Compute the dot product of two or more arrays in a single function call, while automatically selecting the fastest evaluation order. |
| [`vdot`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.vdot.html#numpy.vdot)(a, b) | Return the dot product of two vectors.                       |
| [`inner`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.inner.html#numpy.inner)(a, b) | Inner product of two arrays.                                 |
| [`outer`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.outer.html#numpy.outer)(a, b[, out]) | Compute the outer product of two vectors.                    |
| [`matmul`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.matmul.html#numpy.matmul)(a, b[, out]) | Matrix product of two arrays.                                |
| [`tensordot`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tensordot.html#numpy.tensordot)(a, b[, axes]) | Compute tensor dot product along specified axes for arrays >= 1-D. |
| [`einsum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum.html#numpy.einsum)(subscripts, *operands[, out, dtype, …]) | Evaluates the Einstein summation convention on the operands. |
| [`einsum_path`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.einsum_path.html#numpy.einsum_path)(subscripts, *operands[, optimize]) | Evaluates the lowest cost contraction order for an einsum expression by considering the creation of intermediate arrays. |
| [`linalg.matrix_power`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.matrix_power.html#numpy.linalg.matrix_power)(a, n) | Raise a square matrix to the (integer) power *n*.            |
| [`kron`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.kron.html#numpy.kron)(a, b) | Kronecker product of two arrays.                             |



## Decomposition

| 方法                                                         | 用途                                      |
| ------------------------------------------------------------ | ----------------------------------------- |
| [`linalg.cholesky`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.cholesky.html#numpy.linalg.cholesky)(a) | Cholesky decomposition.                   |
| [`linalg.qr`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.qr.html#numpy.linalg.qr)(a[, mode]) | Compute the qr factorization of a matrix. |
| [`linalg.svd`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html#numpy.linalg.svd)(a[, full_matrices, compute_uv]) | Singular Value Decomposition.             |



## Matrix eigenvalues

| 方法                                                         | 功能                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`linalg.eig`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig)(a) | Compute the eigenvalues and right eigenvectors of a square array. |
| [`linalg.eigh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eigh.html#numpy.linalg.eigh)(a[, UPLO]) | Return the eigenvalues and eigenvectors of a Hermitian or symmetric matrix. |
| [`linalg.eigvals`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals)(a) | Compute the eigenvalues of a general matrix.                 |
| [`linalg.eigvalsh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.eigvalsh.html#numpy.linalg.eigvalsh)(a[, UPLO]) | Compute the eigenvalues of a Hermitian or real symmetric matrix. |



## Norms and other numbers

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`linalg.norm`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.norm.html#numpy.linalg.norm)(x[, ord, axis, keepdims]) | Matrix or vector norm.                                       |
| [`linalg.cond`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.cond.html#numpy.linalg.cond)(x[, p]) | Compute the condition number of a matrix.                    |
| [`linalg.det`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.det.html#numpy.linalg.det)(a) | Compute the determinant of an array.                         |
| [`linalg.matrix_rank`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.matrix_rank.html#numpy.linalg.matrix_rank)(M[, tol, hermitian]) | Return matrix rank of array using SVD method                 |
| [`linalg.slogdet`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.slogdet.html#numpy.linalg.slogdet)(a) | Compute the sign and (natural) logarithm of the determinant of an array. |
| [`trace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.trace.html#numpy.trace)(a[, offset, axis1, axis2, dtype, out]) | Return the sum along diagonals of the array.                 |



## Solving equations and inverting matrices

| [`linalg.solve`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.solve.html#numpy.linalg.solve)(a, b) | Solve a linear matrix equation, or system of linear scalar equations. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`linalg.tensorsolve`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.tensorsolve.html#numpy.linalg.tensorsolve)(a, b[, axes]) | Solve the tensor equation `a x = b` for x.                   |
| [`linalg.lstsq`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html#numpy.linalg.lstsq)(a, b[, rcond]) | Return the least-squares solution to a linear matrix equation. |
| [`linalg.inv`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.inv.html#numpy.linalg.inv)(a) | Compute the (multiplicative) inverse of a matrix.            |
| [`linalg.pinv`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.pinv.html#numpy.linalg.pinv)(a[, rcond]) | Compute the (Moore-Penrose) pseudo-inverse of a matrix.      |
| [`linalg.tensorinv`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.tensorinv.html#numpy.linalg.tensorinv)(a[, ind]) | Compute the ‘inverse’ of an N-dimensional array.             |



# Logic functions

## Truth value testing

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`all`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.all.html#numpy.all)(a[, axis, out, keepdims]) | Test whether all array elements along a given axis evaluate to True. |
| [`any`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.any.html#numpy.any)(a[, axis, out, keepdims]) | Test whether any array element along a given axis evaluates to True. |



## Array contents

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`isfinite`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isfinite.html#numpy.isfinite)(x, /[, out, where, casting, order, …]) | Test element-wise for finiteness (not infinity or not Not a Number). |
| [`isinf`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isinf.html#numpy.isinf)(x, /[, out, where, casting, order, …]) | Test element-wise for positive or negative infinity.         |
| [`isnan`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnan.html#numpy.isnan)(x, /[, out, where, casting, order, …]) | Test element-wise for NaN and return result as a boolean array. |
| [`isnat`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isnat.html#numpy.isnat)(x, /[, out, where, casting, order, …]) | Test element-wise for NaT (not a time) and return result as a boolean array. |
| [`isneginf`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isneginf.html#numpy.isneginf)(x[, out]) | Test element-wise for negative infinity, return result as bool array. |
| [`isposinf`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isposinf.html#numpy.isposinf)(x[, out]) | Test element-wise for positive infinity, return result as bool array. |



## Comparison

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`allclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.allclose.html#numpy.allclose)(a, b[, rtol, atol, equal_nan]) | Returns True if two arrays are element-wise equal within a tolerance. |
| [`isclose`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.isclose.html#numpy.isclose)(a, b[, rtol, atol, equal_nan]) | Returns a boolean array where two arrays are element-wise equal within a tolerance. |
| [`array_equal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equal.html#numpy.array_equal)(a1, a2) | True if two arrays have the same shape and elements, False otherwise. |
| [`array_equiv`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_equiv.html#numpy.array_equiv)(a1, a2) | Returns True if input arrays are shape consistent and all elements equal. |

| 方法                                                         | 用途                                               |
| ------------------------------------------------------------ | -------------------------------------------------- |
| [`greater`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater.html#numpy.greater)(x1, x2, /[, out, where, casting, …]) | Return the truth value of (x1 > x2) element-wise.  |
| [`greater_equal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.greater_equal.html#numpy.greater_equal)(x1, x2, /[, out, where, …]) | Return the truth value of (x1 >= x2) element-wise. |
| [`less`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less.html#numpy.less)(x1, x2, /[, out, where, casting, …]) | Return the truth value of (x1 < x2) element-wise.  |
| [`less_equal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.less_equal.html#numpy.less_equal)(x1, x2, /[, out, where, casting, …]) | Return the truth value of (x1 =< x2) element-wise. |
| [`equal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.equal.html#numpy.equal)(x1, x2, /[, out, where, casting, …]) | Return (x1 == x2) element-wise.                    |
| [`not_equal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.not_equal.html#numpy.not_equal)(x1, x2, /[, out, where, casting, …]) | Return (x1 != x2) element-wise.                    |



# Mathematical functions

## Trigonometric functions

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`sin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sin.html#numpy.sin)(x, /[, out, where, casting, order, …]) | Trigonometric sine, element-wise.                            |
| [`cos`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cos.html#numpy.cos)(x, /[, out, where, casting, order, …]) | Cosine element-wise.                                         |
| [`tan`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tan.html#numpy.tan)(x, /[, out, where, casting, order, …]) | Compute tangent element-wise.                                |
| [`arcsin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arcsin.html#numpy.arcsin)(x, /[, out, where, casting, order, …]) | Inverse sine, element-wise.                                  |
| [`arccos`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arccos.html#numpy.arccos)(x, /[, out, where, casting, order, …]) | Trigonometric inverse cosine, element-wise.                  |
| [`arctan`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan.html#numpy.arctan)(x, /[, out, where, casting, order, …]) | Trigonometric inverse tangent, element-wise.                 |
| [`hypot`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.hypot.html#numpy.hypot)(x1, x2, /[, out, where, casting, …]) | Given the “legs” of a right triangle, return its hypotenuse. |
| [`arctan2`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctan2.html#numpy.arctan2)(x1, x2, /[, out, where, casting, …]) | Element-wise arc tangent of `x1/x2`choosing the quadrant correctly. |
| [`degrees`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.degrees.html#numpy.degrees)(x, /[, out, where, casting, order, …]) | Convert angles from radians to degrees.                      |
| [`radians`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.radians.html#numpy.radians)(x, /[, out, where, casting, order, …]) | Convert angles from degrees to radians.                      |
| [`unwrap`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.unwrap.html#numpy.unwrap)(p[, discont, axis]) | Unwrap by changing deltas between values to 2*pi complement. |
| [`deg2rad`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.deg2rad.html#numpy.deg2rad)(x, /[, out, where, casting, order, …]) | Convert angles from degrees to radians.                      |
| [`rad2deg`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.rad2deg.html#numpy.rad2deg)(x, /[, out, where, casting, order, …]) | Convert angles from radians to degrees.                      |



## Hyperbolic functions

| 方法                                                         | 用途                                     |
| ------------------------------------------------------------ | ---------------------------------------- |
| [`sinh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sinh.html#numpy.sinh)(x, /[, out, where, casting, order, …]) | Hyperbolic sine, element-wise.           |
| [`cosh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cosh.html#numpy.cosh)(x, /[, out, where, casting, order, …]) | Hyperbolic cosine, element-wise.         |
| [`tanh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.tanh.html#numpy.tanh)(x, /[, out, where, casting, order, …]) | Compute hyperbolic tangent element-wise. |
| [`arcsinh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arcsinh.html#numpy.arcsinh)(x, /[, out, where, casting, order, …]) | Inverse hyperbolic sine element-wise.    |
| [`arccosh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arccosh.html#numpy.arccosh)(x, /[, out, where, casting, order, …]) | Inverse hyperbolic cosine, element-wise. |
| [`arctanh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.arctanh.html#numpy.arctanh)(x, /[, out, where, casting, order, …]) | Inverse hyperbolic tangent element-wise. |



## Rounding

| 方法                                                         | 用途                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [`around`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.around.html#numpy.around)(a[, decimals, out]) | Evenly round to the given number of decimals.          |
| [`round_`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.round_.html#numpy.round_)(a[, decimals, out]) | Round an array to the given number of decimals.        |
| [`rint`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.rint.html#numpy.rint)(x, /[, out, where, casting, order, …]) | Round elements of the array to the nearest integer.    |
| [`fix`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fix.html#numpy.fix)(x[, out]) | Round to nearest integer towards zero.                 |
| [`floor`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.floor.html#numpy.floor)(x, /[, out, where, casting, order, …]) | Return the floor of the input, element-wise.           |
| [`ceil`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ceil.html#numpy.ceil)(x, /[, out, where, casting, order, …]) | Return the ceiling of the input, element-wise.         |
| [`trunc`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.trunc.html#numpy.trunc)(x, /[, out, where, casting, order, …]) | Return the truncated value of the input, element-wise. |



## Sums, products, differences

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`prod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.prod.html#numpy.prod)(a[, axis, dtype, out, keepdims, initial]) | Return the product of array elements over a given axis.      |
| [`sum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html#numpy.sum)(a[, axis, dtype, out, keepdims, initial]) | Sum of array elements over a given axis.                     |
| [`nanprod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanprod.html#numpy.nanprod)(a[, axis, dtype, out, keepdims]) | Return the product of array elements over a given axis treating Not a Numbers (NaNs) as ones. |
| [`nansum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nansum.html#numpy.nansum)(a[, axis, dtype, out, keepdims]) | Return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero. |
| [`cumprod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumprod.html#numpy.cumprod)(a[, axis, dtype, out]) | Return the cumulative product of elements along a given axis. |
| [`cumsum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cumsum.html#numpy.cumsum)(a[, axis, dtype, out]) | Return the cumulative sum of the elements along a given axis. |
| [`nancumprod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nancumprod.html#numpy.nancumprod)(a[, axis, dtype, out]) | Return the cumulative product of array elements over a given axis treating Not a Numbers (NaNs) as one. |
| [`nancumsum`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nancumsum.html#numpy.nancumsum)(a[, axis, dtype, out]) | Return the cumulative sum of array elements over a given axis treating Not a Numbers (NaNs) as zero. |
| [`diff`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.diff.html#numpy.diff)(a[, n, axis]) | Calculate the n-th discrete difference along the given axis. |
| [`ediff1d`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ediff1d.html#numpy.ediff1d)(ary[, to_end, to_begin]) | The differences between consecutive elements of an array.    |
| [`gradient`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.gradient.html#numpy.gradient)(f, *varargs, **kwargs) | Return the gradient of an N-dimensional array.               |
| [`cross`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cross.html#numpy.cross)(a, b[, axisa, axisb, axisc, axis]) | Return the cross product of two (arrays of) vectors.         |
| [`trapz`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html#numpy.trapz)(y[, x, dx, axis]) | Integrate along the given axis using the composite trapezoidal rule. |



## Exponents and logarithms

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`exp`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp.html#numpy.exp)(x, /[, out, where, casting, order, …]) | Calculate the exponential of all elements in the input array. |
| [`expm1`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.expm1.html#numpy.expm1)(x, /[, out, where, casting, order, …]) | Calculate `exp(x) - 1` for all elements in the array.        |
| [`exp2`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.exp2.html#numpy.exp2)(x, /[, out, where, casting, order, …]) | Calculate *2\**p* for all *p* in the input array.            |
| [`log`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log.html#numpy.log)(x, /[, out, where, casting, order, …]) | Natural logarithm, element-wise.                             |
| [`log10`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log10.html#numpy.log10)(x, /[, out, where, casting, order, …]) | Return the base 10 logarithm of the input array, element-wise. |
| [`log2`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log2.html#numpy.log2)(x, /[, out, where, casting, order, …]) | Base-2 logarithm of *x*.                                     |
| [`log1p`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.log1p.html#numpy.log1p)(x, /[, out, where, casting, order, …]) | Return the natural logarithm of one plus the input array, element-wise. |
| [`logaddexp`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logaddexp.html#numpy.logaddexp)(x1, x2, /[, out, where, casting, …]) | Logarithm of the sum of exponentiations of the inputs.       |
| [`logaddexp2`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logaddexp2.html#numpy.logaddexp2)(x1, x2, /[, out, where, casting, …]) | Logarithm of the sum of exponentiations of the inputs in base-2. |



## Arithmetic operations

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`add`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.add.html#numpy.add)(x1, x2, /[, out, where, casting, order, …]) | Add arguments element-wise.                                  |
| [`reciprocal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reciprocal.html#numpy.reciprocal)(x, /[, out, where, casting, …]) | Return the reciprocal of the argument, element-wise.         |
| [`positive`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.positive.html#numpy.positive)(x, /[, out, where, casting, order, …]) | Numerical positive, element-wise.                            |
| [`negative`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.negative.html#numpy.negative)(x, /[, out, where, casting, order, …]) | Numerical negative, element-wise.                            |
| [`multiply`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.multiply.html#numpy.multiply)(x1, x2, /[, out, where, casting, …]) | Multiply arguments element-wise.                             |
| [`divide`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.divide.html#numpy.divide)(x1, x2, /[, out, where, casting, …]) | Returns a true division of the inputs, element-wise.         |
| [`power`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.power.html#numpy.power)(x1, x2, /[, out, where, casting, …]) | First array elements raised to powers from second array, element-wise. |
| [`subtract`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.subtract.html#numpy.subtract)(x1, x2, /[, out, where, casting, …]) | Subtract arguments, element-wise.                            |
| [`true_divide`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.true_divide.html#numpy.true_divide)(x1, x2, /[, out, where, …]) | Returns a true division of the inputs, element-wise.         |
| [`floor_divide`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.floor_divide.html#numpy.floor_divide)(x1, x2, /[, out, where, …]) | Return the largest integer smaller or equal to the division of the inputs. |
| [`float_power`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.float_power.html#numpy.float_power)(x1, x2, /[, out, where, …]) | First array elements raised to powers from second array, element-wise. |
| [`fmod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fmod.html#numpy.fmod)(x1, x2, /[, out, where, casting, …]) | Return the element-wise remainder of division.               |
| [`mod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mod.html#numpy.mod)(x1, x2, /[, out, where, casting, order, …]) | Return element-wise remainder of division.                   |
| [`modf`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.modf.html#numpy.modf)(x[, out1, out2], / [[, out, where, …]) | Return the fractional and integral parts of an array, element-wise. |
| [`remainder`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.remainder.html#numpy.remainder)(x1, x2, /[, out, where, casting, …]) | Return element-wise remainder of division.                   |
| [`divmod`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.divmod.html#numpy.divmod)(x1, x2[, out1, out2], / [[, out, …]) | Return element-wise quotient and remainder simultaneously.   |



# Random sampling (numpy.random)

## Simple random data

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`rand`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html#numpy.random.rand)(d0, d1, …, dn) | Random values in a given shape.                              |
| [`randn`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html#numpy.random.randn)(d0, d1, …, dn) | Return a sample (or samples) from the “standard normal” distribution. |
| [`randint`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randint.html#numpy.random.randint)(low[, high, size, dtype]) | Return random integers from *low* (inclusive) to *high* (exclusive). |
| [`random_integers`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.random_integers.html#numpy.random.random_integers)(low[, high, size]) | Random integers of type np.int between *low* and *high*, inclusive. |
| [`random_sample`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.random_sample.html#numpy.random.random_sample)([size]) | Return random floats in the half-open interval [0.0, 1.0).   |
| [`random`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.random.html#numpy.random.random)([size]) | Return random floats in the half-open interval [0.0, 1.0).   |
| [`ranf`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.ranf.html#numpy.random.ranf)([size]) | Return random floats in the half-open interval [0.0, 1.0).   |
| [`sample`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.sample.html#numpy.random.sample)([size]) | Return random floats in the half-open interval [0.0, 1.0).   |
| [`choice`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html#numpy.random.choice)(a[, size, replace, p]) | Generates a random sample from a given 1-D array             |
| [`bytes`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.bytes.html#numpy.random.bytes)(length) | Return random bytes.                                         |



## Permutations

| 方法                                                         | 用途                                                     |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [`shuffle`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.shuffle.html#numpy.random.shuffle)(x) | Modify a sequence in-place by shuffling its contents.    |
| [`permutation`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.permutation.html#numpy.random.permutation)(x) | Randomly permute a sequence, or return a permuted range. |



## Distributions

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`beta`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.beta.html#numpy.random.beta)(a, b[, size]) | Draw samples from a Beta distribution.                       |
| [`binomial`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html#numpy.random.binomial)(n, p[, size]) | Draw samples from a binomial distribution.                   |
| [`chisquare`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.chisquare.html#numpy.random.chisquare)(df[, size]) | Draw samples from a chi-square distribution.                 |
| [`dirichlet`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.dirichlet.html#numpy.random.dirichlet)(alpha[, size]) | Draw samples from the Dirichlet distribution.                |
| [`exponential`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.exponential.html#numpy.random.exponential)([scale, size]) | Draw samples from an exponential distribution.               |
| [`f`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.f.html#numpy.random.f)(dfnum, dfden[, size]) | Draw samples from an F distribution.                         |
| [`gamma`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.gamma.html#numpy.random.gamma)(shape[, scale, size]) | Draw samples from a Gamma distribution.                      |
| [`geometric`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.geometric.html#numpy.random.geometric)(p[, size]) | Draw samples from the geometric distribution.                |
| [`gumbel`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.gumbel.html#numpy.random.gumbel)([loc, scale, size]) | Draw samples from a Gumbel distribution.                     |
| [`hypergeometric`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.hypergeometric.html#numpy.random.hypergeometric)(ngood, nbad, nsample[, size]) | Draw samples from a Hypergeometric distribution.             |
| [`laplace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.laplace.html#numpy.random.laplace)([loc, scale, size]) | Draw samples from the Laplace or double exponential distribution with specified location (or mean) and scale (decay). |
| [`logistic`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.logistic.html#numpy.random.logistic)([loc, scale, size]) | Draw samples from a logistic distribution.                   |
| [`lognormal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.lognormal.html#numpy.random.lognormal)([mean, sigma, size]) | Draw samples from a log-normal distribution.                 |
| [`logseries`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.logseries.html#numpy.random.logseries)(p[, size]) | Draw samples from a logarithmic series distribution.         |
| [`multinomial`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multinomial.html#numpy.random.multinomial)(n, pvals[, size]) | Draw samples from a multinomial distribution.                |
| [`multivariate_normal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.multivariate_normal.html#numpy.random.multivariate_normal)(mean, cov[, size, …) | Draw random samples from a multivariate normal distribution. |
| [`negative_binomial`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.negative_binomial.html#numpy.random.negative_binomial)(n, p[, size]) | Draw samples from a negative binomial distribution.          |
| [`noncentral_chisquare`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.noncentral_chisquare.html#numpy.random.noncentral_chisquare)(df, nonc[, size]) | Draw samples from a noncentral chi-square distribution.      |
| [`noncentral_f`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.noncentral_f.html#numpy.random.noncentral_f)(dfnum, dfden, nonc[, size]) | Draw samples from the noncentral F distribution.             |
| [`normal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html#numpy.random.normal)([loc, scale, size]) | Draw random samples from a normal (Gaussian) distribution.   |
| [`pareto`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.pareto.html#numpy.random.pareto)(a[, size]) | Draw samples from a Pareto II or Lomax distribution with specified shape. |
| [`poisson`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.poisson.html#numpy.random.poisson)([lam, size]) | Draw samples from a Poisson distribution.                    |
| [`power`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.power.html#numpy.random.power)(a[, size]) | Draws samples in [0, 1] from a power distribution with positive exponent a - 1. |
| [`rayleigh`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rayleigh.html#numpy.random.rayleigh)([scale, size]) | Draw samples from a Rayleigh distribution.                   |
| [`standard_cauchy`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.standard_cauchy.html#numpy.random.standard_cauchy)([size]) | Draw samples from a standard Cauchy distribution with mode = 0. |
| [`standard_exponential`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.standard_exponential.html#numpy.random.standard_exponential)([size]) | Draw samples from the standard exponential distribution.     |
| [`standard_gamma`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.standard_gamma.html#numpy.random.standard_gamma)(shape[, size]) | Draw samples from a standard Gamma distribution.             |
| [`standard_normal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.standard_normal.html#numpy.random.standard_normal)([size]) | Draw samples from a standard Normal distribution (mean=0, stdev=1). |
| [`standard_t`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.standard_t.html#numpy.random.standard_t)(df[, size]) | Draw samples from a standard Student’s t distribution with *df*degrees of freedom. |
| [`triangular`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.triangular.html#numpy.random.triangular)(left, mode, right[, size]) | Draw samples from the triangular distribution over the interval `[left, right]`. |
| [`uniform`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.uniform.html#numpy.random.uniform)([low, high, size]) | Draw samples from a uniform distribution.                    |
| [`vonmises`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.vonmises.html#numpy.random.vonmises)(mu, kappa[, size]) | Draw samples from a von Mises distribution.                  |
| [`wald`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.wald.html#numpy.random.wald)(mean, scale[, size]) | Draw samples from a Wald, or inverse Gaussian, distribution. |
| [`weibull`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.weibull.html#numpy.random.weibull)(a[, size]) | Draw samples from a Weibull distribution.                    |
| [`zipf`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.zipf.html#numpy.random.zipf)(a[, size]) | Draw samples from a Zipf distribution                        |



# Sorting, searching , and counting

## Sorting

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`sort`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sort.html#numpy.sort)(a[, axis, kind, order]) | Return a sorted copy of an array.                            |
| [`lexsort`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.lexsort.html#numpy.lexsort)(keys[, axis]) | Perform an indirect stable sort using a sequence of keys.    |
| [`argsort`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argsort.html#numpy.argsort)(a[, axis, kind, order]) | Returns the indices that would sort an array.                |
| [`ndarray.sort`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.sort.html#numpy.ndarray.sort)([axis, kind, order]) | Sort an array, in-place.                                     |
| [`msort`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.msort.html#numpy.msort)(a) | Return a copy of an array sorted along the first axis.       |
| [`sort_complex`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sort_complex.html#numpy.sort_complex)(a) | Sort a complex array using the real part first, then the imaginary part. |
| [`partition`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.partition.html#numpy.partition)(a, kth[, axis, kind, order]) | Return a partitioned copy of an array.                       |
| [`argpartition`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argpartition.html#numpy.argpartition)(a, kth[, axis, kind, order]) | Perform an indirect partition along the given axis using the algorithm specified by the *kind*keyword. |



## Searching

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`argmax`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmax.html#numpy.argmax)(a[, axis, out]) | Returns the indices of the maximum values along an axis.     |
| [`nanargmax`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanargmax.html#numpy.nanargmax)(a[, axis]) | Return the indices of the maximum values in the specified axis ignoring NaNs. |
| [`argmin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argmin.html#numpy.argmin)(a[, axis, out]) | Returns the indices of the minimum values along an axis.     |
| [`nanargmin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanargmin.html#numpy.nanargmin)(a[, axis]) | Return the indices of the minimum values in the specified axis ignoring NaNs. |
| [`argwhere`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.argwhere.html#numpy.argwhere)(a) | Find the indices of array elements that are non-zero, grouped by element. |
| [`nonzero`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nonzero.html#numpy.nonzero)(a) | Return the indices of the elements that are non-zero.        |
| [`flatnonzero`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.flatnonzero.html#numpy.flatnonzero)(a) | Return indices that are non-zero in the flattened version of a. |
| [`where`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html#numpy.where)(condition, [x, y]) | Return elements, either from *x* or *y*, depending on *condition*. |
| [`searchsorted`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.searchsorted.html#numpy.searchsorted)(a, v[, side, sorter]) | Find indices where elements should be inserted to maintain order. |
| [`extract`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.extract.html#numpy.extract)(condition, arr) | Return the elements of an array that satisfy some condition. |



## Counting

| 方法                                                         | 用途                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------ |
| [`count_nonzero`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.count_nonzero.html#numpy.count_nonzero)(a[, axis]) | Counts the number of non-zero values in the array `a`. |



# Statistics

## Order statistics

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`amin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.amin.html#numpy.amin)(a[, axis, out, keepdims, initial]) | Return the minimum of an array or minimum along an axis.     |
| [`amax`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.amax.html#numpy.amax)(a[, axis, out, keepdims, initial]) | Return the maximum of an array or maximum along an axis.     |
| [`nanmin`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmin.html#numpy.nanmin)(a[, axis, out, keepdims]) | Return minimum of an array or minimum along an axis, ignoring any NaNs. |
| [`nanmax`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmax.html#numpy.nanmax)(a[, axis, out, keepdims]) | Return the maximum of an array or maximum along an axis, ignoring any NaNs. |
| [`ptp`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ptp.html#numpy.ptp)(a[, axis, out, keepdims]) | Range of values (maximum - minimum) along an axis.           |
| [`percentile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.percentile.html#numpy.percentile)(a, q[, axis, out, …]) | Compute the qth percentile of the data along the specified axis. |
| [`nanpercentile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanpercentile.html#numpy.nanpercentile)(a, q[, axis, out, …]) | Compute the qth percentile of the data along the specified axis, while ignoring nan values. |
| [`quantile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.quantile.html#numpy.quantile)(a, q[, axis, out, overwrite_input, …]) | Compute the [`](https://docs.scipy.org/doc/numpy/reference/routines.statistics.html#id1)q`th quantile of the data along the specified axis…versionadded:: 1.15.0. |
| [`nanquantile`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanquantile.html#numpy.nanquantile)(a, q[, axis, out, …]) | Compute the qth quantile of the data along the specified axis, while ignoring nan values. |



## Averages and variance

| 方法                                                         | 用途                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`median`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.median.html#numpy.median)(a[, axis, out, overwrite_input, keepdims]) | Compute the median along the specified axis.                 |
| [`average`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.average.html#numpy.average)(a[, axis, weights, returned]) | Compute the weighted average along the specified axis.       |
| [`mean`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html#numpy.mean)(a[, axis, dtype, out, keepdims]) | Compute the arithmetic mean along the specified axis.        |
| [`std`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.std.html#numpy.std)(a[, axis, dtype, out, ddof, keepdims]) | Compute the standard deviation along the specified axis.     |
| [`var`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.var.html#numpy.var)(a[, axis, dtype, out, ddof, keepdims]) | Compute the variance along the specified axis.               |
| [`nanmedian`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmedian.html#numpy.nanmedian)(a[, axis, out, overwrite_input, …]) | Compute the median along the specified axis, while ignoring NaNs. |
| [`nanmean`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanmean.html#numpy.nanmean)(a[, axis, dtype, out, keepdims]) | Compute the arithmetic mean along the specified axis, ignoring NaNs. |
| [`nanstd`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanstd.html#numpy.nanstd)(a[, axis, dtype, out, ddof, keepdims]) | Compute the standard deviation along the specified axis, while ignoring NaNs. |
| [`nanvar`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.nanvar.html#numpy.nanvar)(a[, axis, dtype, out, ddof, keepdims]) | Compute the variance along the specified axis, while ignoring NaNs |



## Correleting

| 方法                                                         | 用途                                                    |
| ------------------------------------------------------------ | ------------------------------------------------------- |
| [`corrcoef`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.corrcoef.html#numpy.corrcoef)(x[, y, rowvar, bias, ddof]) | Return Pearson product-moment correlation coefficients. |
| [`correlate`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.correlate.html#numpy.correlate)(a, v[, mode]) | Cross-correlation of two 1-dimensional sequences.       |
| [`cov`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.cov.html#numpy.cov)(m[, y, rowvar, bias, ddof, fweights, …]) | Estimate a covariance matrix, given data and weights.   |