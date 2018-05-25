#
#   This is the Robotics Language compiler
#
#   Output.py: Generates HTML Gui's
#
#   Created on: June 22, 2017
#       Author: Gabriel A. D. Lopes
#      Licence: Apache 2.0
#    Copyright: 2014-2017 Robot Care Systems BV, The Hague, The Netherlands. All rights reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
import sys
from RoboticsLanguage.Base import Utilities

def output(code, parameters):

  # save the node name for the templates
  parameters['node']['name'] = Utilities.option(code.xpath('/node')[0], 'name').text

  # run template engine to generate node code
  if not Utilities.templateEngine(code, parameters, {'nodename': Utilities.underscore(parameters['node']['name'])}, os.path.dirname(
          __file__) + '/Templates', parameters['globals']['deploy']):
    sys.exit(1)
