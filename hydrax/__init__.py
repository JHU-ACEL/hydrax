import os

# Load before ``jax`` so early imports of ``hydrax._paths.ROOT`` / ``hydrax.ROOT`` see a path.
from ._paths import ROOT

import jax

# Set XLA flags for better performance
os.environ["XLA_FLAGS"] = "--xla_gpu_triton_gemm_any=true "

# Enable persistent compilation cache
jax.config.update("jax_compilation_cache_dir", "/tmp/jax_cache")
