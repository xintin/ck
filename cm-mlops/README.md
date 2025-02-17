# CM MLOps repository 

[![CM repository](https://img.shields.io/badge/Collective%20Mind-compatible-blue)](https://github.com/mlcommons/ck/tree/master/cm)
[![CM artifact](https://img.shields.io/badge/Artifact-automated%20and%20reusable-blue)](https://github.com/mlcommons/ck/tree/master/cm)

This repository contains portable scripts
in the [CM format](https://github.com/mlcommons/ck) to unify and interconnect 
different MLOps and DevOps tools acrossd diverse software and hardware stacks.
See the catalog [here](https://github.com/mlcommons/ck/tree/master/cm-mlops/script).

All such cross-platform scripts have a unified API, human readable CLI and extensible JSON/YAML meta description
making it possible to reuse them in different projects and chain them together 
into powerful, efficient and portable automation workflows, applications and web services
adaptable to continuously changing software and hardware.

We use and extend this repository in the [MLPerf education and reproducibility workgroup](../docs/mlperf-education-workgroup.md) 
as a common playground and a common language to help researchers and engineers
learn how to modularize complex software systems (such as AI and ML) 
and automate their benchmarking, optimization, co-design and deployment.

Read about the CM concept [here](https://github.com/mlcommons/ck) 
and follow [this tutorial](../cm/docs/tutorial-scripts.md) 
to install CM framework and understand CM concepts.



## Catalog of portable CM scripts

### Compilers
* [gcc](script/get-gcc)
* [llvm](script/get-llvm)
* [cuda](script/get-cuda)

### ML models
* [resnet50 onnx](script/get-ml-model-resnet50-onnx), [pytorch](script/get-ml-model-resnet50-pytorch) and [tensorflow](script/get-ml-model-resnet50-tf) (fp32)
* [retinanet onnx and pytorch](script/get-ml-model-retinanet) (fp32)
### ML datasets
* [imagenet 2012 validation set](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-val) (1,500,50000 images)
* [imagenet preprocessed](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-imagenet-preprocessed)
* [openimages](https://github.com/mlcommons/ck/tree/master/cm-mlops/script/get-openimages-original)
### ML engines
* [tensorflow](script/get-tensorflow)
* [onnxruntime](script/get-onnxruntime)
* [pytorch](script/get-pytorch)
* [tvm](script/get-tvm)
### Apps
* [Image classification onnx](script/app-image-classification-onnx-py), [onnx cpp](script/app-image-classification-onnx-cpp), [pytorch](script/app-image-classification-torch-py)
* [Image corner detection]()
* [MLPerf inference vision run and submission generation from reference code](script/generate-mlc-inference-submission)
* [MLPerf image classification and submission generation from cpp code](script/app-mlperf-inference-cpp)
### Benchmarks
* [MLPerf inference image classification, object detection](script/app-mlperf-inference-vision-reference)
### Aux tools
* [zephyr](script/get-zephyr)
* [zephyr-sdk](script/get-zephyr-sdk)
* [bazel](script/get-bazel)
* [dnnl](script/get-lib-dnnl)
### Containers
* [docker for Ubuntu 18.04, 20.04, 22.04 and RHEL9](script/build-dockerfile/dockerfiles)
