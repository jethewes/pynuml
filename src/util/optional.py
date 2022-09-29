def requires_package(package: str,
                     name: str) -> None:
    from importlib.util import find_spec
    if find_spec(package) is None:
        print(f'Error: {name} not installed. If installing with pip,')
        print('use "pip install pynuml[torch] to install PyTorch dependencies.')
        sys.exit(1)

def requires_torch() -> None:
    requires_package('torch', 'PyTorch')
    import torch

def requires_pyg() -> None:
    requires_package('torch_geometric', 'PyG')
    import torch_geometric as pyg

