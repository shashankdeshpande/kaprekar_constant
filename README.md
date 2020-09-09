# Kaprekar's constant (6174)
6174 is known as Kaprekar's constant after the Indian  mathematician D. R. Kaprekar. This number is known for the following rule:
- Take any four-digit number (at least two digits should be different)
- Arrange the digits in descending and ascending order to get two new four-digit numbers
- Now, subtract the smaller number from the bigger number
- Go back to step 2 and repeat

This process is called Kaprekar's routine. The routine states that you'll always reach number 6174 in at most 7 iterations and once you reach 6174, the process will continue generating the same number. How cool is that?
## [Installation](#installation)
Install directly from the GitHub repository
```bash
pip install git+https://github.com/shashankdeshpande/kaprekar_constant.git 
```
## [Usage](#usage)
#### [Import package](#import):
```python
>>> import kaprekar_constant as kc
```
#### [Perform Kaprekar Routine](#k_routine):
```python
>>> obj = kc.kaprekar_routine(1913)
>>> obj
<kaprekar_constant.object.Kaprekar at 0x7f1ae2f085c0>
```
#### [Check results](#check):
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
## [References](#references)
- https://en.wikipedia.org/wiki/6174_(number)
- https://mathworld.wolfram.com/KaprekarRoutine.html
- https://plus.maths.org/content/mysterious-number-6174
