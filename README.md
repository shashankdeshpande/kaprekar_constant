# Kaprekar's constant (6174)

## Installation
Install directly from the GitHub repository
```bash
pip install git+https://github.com/shashankdeshpande/kaprekar_constant.git 
```

## Usage
**Import package:**
```python
>>> import kaprekar_constant as kc
```
**Perform Kaprekar Routine:**
```python
>>> obj = kc.kaprekar_routine(1913)
>>> obj
<kaprekar_constant.object.Kaprekar at 0x7f1ae2f085c0>
```
**Process result:**
```python
>>> obj.steps
['9311 - 1139 = 8172',
 '8721 - 1278 = 7443',
 '7443 - 3447 = 3996',
 '9963 - 3699 = 6264',
 '6642 - 2466 = 4176',
 '7641 - 1467 = 6174']
>>> obj.step_count
6
>>> obj.constant
6174
```
