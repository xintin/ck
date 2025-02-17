# Get MLCommons Inference Source
This [CM script](https://github.com/mlcommons/ck/blob/master/cm/docs/tutorial-scripts.md) git clones the [MLCommons Inference repository](https://github.com/mlcommons/inference).

## Commands
To install
```
cm run script --tags=get,mlperf,inference,src,[VARIATION] --version=[VERSION] 
```
where [VARIATION] is one of
* `default:` Works with the official MLCommons inference repository. Uses `short-history` variation
* `patch:` Applies the `git.patch` to the cloned git repository
* `octoml:` Works with the OctoML fork of the MLCommons inference repository. Uses `short-history` variation
* `short-history:` Uses a git depth of last 10 commits (significantly reduces the download size)
* `full-history:` Uses the full git history
* `recurse-submodules:` Downloads all the submodules

[VERSION] is one of
* `master:` Uses the master branch 
* `r2.1:`  Uses the release branch used for MLCommons inference 2.1 round

## Exported Variables
* `CM_MLC_INFERENCE_SOURCE`: Directory path of the cloned inference repository
* `CM_MLC_INFERENCE_VISION_PATH`: Directory path to the vision folder inside the inference repository
* `PYTHONPATH`: Is appended with the paths to vision module and the submission tools module
* `CM_MLPERF_INFERENCE_MODELS`: This `state` variable contains the configuration of the MLPerf models as per the selected version

## Supported and Tested OS
1. Ubuntu 18.04, 20.04, 22.04
2. RHEL 9
