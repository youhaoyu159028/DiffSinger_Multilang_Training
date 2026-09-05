#!/usr/bin/env python3
import importlib.util, json, os, platform, sys

def main():
    result = {'python': sys.version, 'platform': platform.platform(), 'checks': {}}
    try:
        import torch
        result['torch'] = torch.__version__
        result['checks']['torch_import'] = True
        cuda = bool(torch.cuda.is_available())
        result['checks']['cuda_available'] = cuda
        if cuda:
            result['gpu'] = torch.cuda.get_device_name(0)
            result['vram_gib'] = round(torch.cuda.get_device_properties(0).total_memory / 1024**3, 2)
            x = torch.ones((8, 8), device='cuda')
            y = x @ x
            result['checks']['cuda_operation'] = bool(y.is_cuda and float(y[0,0]) > 0)
        else:
            result['checks']['cuda_operation'] = False
    except Exception as e:
        result['checks']['torch_import'] = False; result['torch_error'] = repr(e)
    for mod in ['yaml', 'numpy', 'soundfile', 'onnxruntime']:
        result['checks'][mod] = importlib.util.find_spec(mod) is not None
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if all(result['checks'].values()) else 1

if __name__ == '__main__': raise SystemExit(main())
