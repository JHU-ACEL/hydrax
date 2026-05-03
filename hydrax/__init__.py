import os
from pathlib import Path

# Package root — defined before ``import jax`` so submodules that import
# ``from hydrax import ROOT`` during hydrax's own ``__init__`` (e.g. circular
# loads via optional stacks) always see a valid attribute.
ROOT = str(Path(__file__).resolve().parent)

import jax

# Set XLA flags for better performance
os.environ["XLA_FLAGS"] = "--xla_gpu_triton_gemm_any=true "

# Enable persistent compilation cache
jax.config.update("jax_compilation_cache_dir", "/tmp/jax_cache")
