[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/C9-mVD2y)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11116770&assignment_repo_type=AssignmentRepo)
# Algorithm1 Homework4
This example project is written in Python, and tested with pytest.

### The assignment
- 입력으로 코인 종류를 담은 리스트와 거스름돈을 받으면 최소의 거스름 동전 개수 합과 각 동전의 개수를 반환하는 함수 coin_change()를 파일 coinChange.py에 구현한다. 첫 번째 인자인 리스트는 동전 금액의 내림 차순으로 정렬되어 있으며 각 금액은 1보다 크거나 같은 정수라야 한다. 리스트의 마지막 동전 금액인 1로 고정한다. coin_change()는 다음과 같다.

`coin_change(list, m)`

예를 들어, 다음을 실행하면 9, [7, 0, 0, 2]를 반환한다. 

`coin_change([100, 10, 5, 1], 66)`

현재 제공되는 coinChange.py 파일은 아직 완전하게 수행되지 않는다.

### Setup command
`sudo -H pip3 install pytest`

### Run command
`pytest coinChange_test1.py`

`pytest coinChange_test2.py`

`pytest coinChange_test3.py`

### Notes
- pip's install path is not included in the PATH var by default, so without installing via `sudo -H`, pytest would be unaccessible.
