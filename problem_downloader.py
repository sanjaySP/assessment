# -*- coding: utf-8 -*-

import subprocess
class Kaggle(object):
    """A wraper for kaggle_cli to download the dataset from kaggle."""
    def __init__(self, username, password):
        """ kaggle wraper takes username and password to login to kaggle."""
        self.username = username
        self.password = password
    def download(self, owner, dataset):
        """generate a query and download.
        input: owner, dataset
        output: None
        function: download and save the dataset."""
        print 'please wait dataset downloading...'
        query = "kg dataset -u {user} -p {passw} -o {owner} -d {data}"
        query = query.format(user=self.username, \
                             passw=self.password, \
                             owner=owner, \
                             data=dataset).split()
        result = subprocess.check_output(query)
        print result

if __name__ == '__main__':
# =============================================================================
#     Writing the test case in main.
# =============================================================================
    KG = Kaggle('sanjay.poongs@gmail.com', 'sanjay0718')
    KG.download('madhab', 'jobposts')
    