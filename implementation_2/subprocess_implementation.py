import subprocess
import requests
import base64

def get_code(owner, repo, file_path, access_token):
    """This function gets code from GitHub using the Github API
    and the python requests module and returns it as
    a string"""
    # get the learner url from GitHub
    learner_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(learner_url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch learner's file, response code: {response.status_code}")
        return None

    # convert the content of the response to json
    file_content = response.json().get('content')
    
    # decode the content since it was encoded using base64
    file_content = base64.b64decode(file_content).decode('utf-8')
    return file_content

def run_tests(learner_code, test_cases):
    """This function compares the code retrieved from GitHub
    to our test cases and compares the output"""
    for input_data, expected_output in test_cases:
        try:
            # get the output from learner's code and input data
            output = subprocess.check_output(["python", "-c", learner_code], input=input_data.encode(), timeout=5, universal_newlines=True)
            # compare the output eith the expected output
            if output.strip() == expected_output.strip():
                print("Tests passed!")
            else:
                print("Test failed. Expected: ", expected_output, "Got: ", output)
        except subprocess.TimeoutExpired:
            print("Test failed. Execution time exceeded.")
        except Exception as e:
            print("Test failes. Error occured:", e)


# Exapmle usage
def main():
    # fetch learner's code
    learner_code = get_code("am-derrick", "auto-correct-code-checker", "implementation_2/factorial_recursive.py", "xxx")
    if learner_code is None:
        return

    # load the test cases
    with open("test_cases_factorial.txt", "r") as file:
        test_cases = [tuple(line.strip().split(",")) for line in file]

    # run tests
    run_tests(learner_code, test_cases)

if __name__ == "__main__":
    main()
