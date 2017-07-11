# VPR NEXT

VPR Next is Vermont Public Radio's 2016 capital campaign. This site was designed by [Oxbow](http://www.oxbow.co/#intro).

## Notes on the Project

### One-time setup work:

1. Make sure you have Python 2.7 installed.
1. Clone the repo locally. `git clone git@github.com:vprnet/next.git`
1. [Install `pip`](https://pip.pypa.io/en/latest/installing.html)
1. Install virtualenv. `pip install virtualenv`
1. Create a virtual environment for the app. `virtualenv venv`
1. Enter the virtual environment. `source venv/bin/activate`
1. Install the app requirements. `pip install -r requirements.txt`

### For regular updates, start here:

1. Change into the project directory. `cd next`
1. Enter the virtual environment. `source venv/bin/activate`
1. To run locally, just hit a quick	`python app/index.py` and head to `127.0.0.1:5000`
1. To push to production on Amazon S3, run `python app/index.py build`
