__author__ = 'Nyukers'

import clr
import os.path
project_dir = os.path.dirname(os.path.abspath(__file__))
import sys
sys.path.append(os.path.join(project_dir, "TestStack.White.9.2.0.11\\lib\\net40\\"))
sys.path.append(os.path.join(project_dir, "Castle.Core.3.1.0\\lib\\net40-client\\"))
clr.AddReferenceByName('TestStack.White')

from TestStack.White import Application
from TestStack.White.UIItems.Finders import *

def test_smth():
    print("okokok")
    application = Application.Launch("notepad.exe")
    main_window = application.GetWindow("Free Adrress Book")
    main_window.Get(SearchCriteria.ByAutomationId("groupbutton")).Click()
