import requests
import base64

def compare_code(owner, repo, file_path, rubric_path, access_token):
    # get the learner url from GitHub
    learner_url = f"https://api.github.com/repos/{owner}/{repo}/contents/{file_path}"
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(learner_url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch learner's file, response code: {response.status_code}")
        return

    # convert the content of the response to json
    learner_file_content = response.json().get('content')
    
    # decode the content since it was encoded using base64
    learner_file_content = base64.b64decode(learner_file_content).decode('utf-8')

    # locate and open the rubcric code and compare with the learner code
    with open(rubric_path, 'r') as file:
        rubric_code = file.read()

    learner_lines = learner_file_content.splitlines()
    rubric_lines = rubric_code.splitlines()

    if len(learner_lines) != len(rubric_lines):
        print("Number of lines in the learner's code does not match.")
        return False

    for i in range(len(learner_lines)):
        if learner_lines[i] != rubric_lines[i]:
            print(f"Difference found at line {i+1}:")
            print(f"Learner's code: {learner_lines[i]}")
            print(f"Rubric code: {rubric_lines[i]}")
            return False

    print("Learner's code matches the reference code.")
    return True


# example of usage
# compare_code("learner_username", "learner_repository", "path/to/learner_file.py", "path/to/reference_code.py", "YOUR_PERSONAL_ACCESS_TOKEN")
compare_code("am-derrick", "trading_app", "CSVReader.h", "CSVReader.h", "xXXXxxxxXXX")
