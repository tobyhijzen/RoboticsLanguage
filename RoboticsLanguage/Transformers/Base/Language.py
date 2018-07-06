# -*- coding: utf-8 -*-
#
#   This is the Robotics Language compiler
#
#   Language.py: Definitions of the base language
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

from RoboticsLanguage.Base.Types import arguments, optional, returns

language = {

    #######################################################################
    # Atomic types

    'string': {
        'localisation':
        {
            'pt': 'texto'
        },
        'documentation':
        {
        }
    },
    'number': {
        'localisation':
        {
        },
        'documentation':
        {
        }
    },

    'integer': {
        'localisation':
        {
            'pt': 'inteiro'
        },
        'documentation':
        {
        }
    },

    'natural': {
        'localisation':
        {
            'pt': 'natural'
        },
        'documentation':
        {
        }
    },

    'boolean': {
        'localisation':
        {
        },
        'documentation':
        {
        }
    },

    'real': {
        'localisation':
        {
            'pt': 'real'
        },
        'documentation':
        {
        }
    },

    #######################################################################
    # Language structural elements

    'option': {
        'definition': {
            'arguments': arguments('anything'),
            'returns': returns('same')
        },
        'localisation':
        {
            'pt': 'parâmetro'
        },
        'documentation':
        {
        }
    },

    'anything': {
        'definition': {
            'arguments': arguments('anything'),
            'returns': returns('none')
        },
    },


    'block': {
        'definition': {
            'arguments': arguments('anything'),
            'returns': returns('block')
        },
    },

    #######################################################################
    # Base functions


    'node': {
        'definition': {
            'arguments': arguments('anything'),
            'optional': {
                'rate': optional('number', 1),
                'name': optional('string', 'unnamed'),
                'initialise': optional('anything', None),
                'finalise': optional('anything', None),
                'definitions': optional('anything', None),
            },
            'returns': returns('node')
        },
        'localisation':
        {
            'pt': 'nó',
            'el': 'κόμβος'
        },
        'documentation':
        {
            'title': 'The main software node',
            'description': 'This is the main RoL node. Definitions, initialisation, events, etc., are defined here.',
            'usage': 'node(\n  name:"hello world",\n  initialise(print("hello world"))\n)'
        }
    },
    'print': {
        'definition': {
            'arguments': arguments('string+'),
            'optional': {'level': optional('string', 'info')},
            'returns': returns('none')
        },
        'output':
        {
            'HTMLDocumentation': 'print({{children|first}})',
            'HTMLGUI': '',
            'RoL': 'print({{children|first}})',
        },
        'localisation':
        {
            'pt': 'imprimir',
            'el': 'εκτύπωσε',
            'nl': 'afdrukken'
        },
        'documentation':
        {
        }
    },

    #
    # 'Reals': {
    #     'definition': {
    #         'optionalArguments': {'bits': singleInteger},
    #         'optionalDefaults': {'bits': 32},
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'output':
    #     {
    #         'HTMLDocumentation': 'Real',
    #         'HTMLGUI': 'Real',
    #         'RoL': 'Reals',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'real'
    #     },
    #     'documentation':
    #     {
    #         'title': 'Real numbers type',
    #         'description': 'A type representing real numbers. Assumptions on the number of bits used by the compiler to represent a real number is given as information in the editor.',
    #         'usage': 'x in Reals'
    #     }
    # },
    #
    # 'Integers': {
    #     'definition': {
    #         'optionalArguments': {'bits': singleInteger},
    #         'optionalDefaults': {'bits': 32},
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'output':
    #     {
    #         'HTMLDocumentation': 'Integer',
    #         'HTMLGUI': 'Integer',
    #         'RoL': 'Integers',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'inteiro'
    #     },
    #     'documentation':
    #     {
    #         'title': 'Integer numbers type',
    #         'description': 'A type representing integer numbers. Assumptions on the number of bits used by the compiler to represent an integer number is given as information in the editor.',
    #         'usage': 'x in Integers'
    #     }
    # },
    #
    # 'Naturals': {
    #     'definition': {
    #         'optionalArguments': {'bits': singleNatural},
    #         'optionalDefaults': {'bits': 32},
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'output':
    #     {
    #         'HTMLDocumentation': 'Natural',
    #         'HTMLGUI': 'Natural',
    #         'RoL': 'Naturals',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'natural'
    #     },
    #     'documentation':
    #     {
    #         'title': 'Natural numbers type',
    #         'description': 'A type representing natural numbers. Assumptions on the number of bits used by the compiler to represent an natural number is given as information in the editor.',
    #         'usage': 'x in Naturals'
    #     }
    # },
    #
    # 'Strings': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'output':
    #     {
    #         'HTMLDocumentation': 'String',
    #         'HTMLGUI': 'String',
    #         'RoL': 'Strings',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'texto'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'Booleans': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'output':
    #     {
    #         'HTMLDocumentation': 'Boolean',
    #         'HTMLGUI': 'Boolean',
    #         'RoL': 'Booleans',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'boleano'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'Signals': {
    #     'localisation':
    #     {
    #         'pt': 'sinal'
    #     },
    #     'documentation':
    #     {
    #         'title': 'A time or event based signal',
    #         'description': 'Defines a signal type.',
    #         'usage': 'x in Signals(Reals,rostopic:\'/test/signal\')'
    #     }
    # },
    #
    #
    # 'vector': {
    #     'localisation':
    #     {
    #         'pt': 'vector'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'set': {
    #     'localisation':
    #     {
    #         'pt': 'conjunto'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'associativeArray': {
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #         'title': 'Set',
    #         'description': 'A set of values',
    #         'usage': 'a = { b, c ,d }'
    #     }
    # },
    #
    # 'function': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'return': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'functionDefinition': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'arguments': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'content': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'returns': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'variable': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'output':
    #     {
    #         'HTMLDocumentation': '{{attributes["name"]}}',
    #         'HTMLGUI': '{{attributes["name"]}}',
    #         'RoL': '{{attributes["name"]}}',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'variável'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    #
    # 'element': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'localisation':
    #     {
    #         'pt': 'elemento'
    #     },
    #     'documentation':
    #     {
    #         'title': 'Element of a set of type',
    #         'description': 'Defines a variable to be an element of a set or a type. If a set is provided, then the variable takes the type of the elements of the set',
    #         'usage': 'x in Reals'
    #     }
    # },
    #
    # 'defineFunction': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'block': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnCodeBlock
    #     },
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'anything': {
    #     'definition': {
    #         'argumentTypes': anything,
    #         'returnType': returnNothing
    #     },
    #     'localisation':
    #     {
    #     },
    #     'documentation':
    #     {
    #     }
    # },


    #
    # 'cycle': {
    #     'output':
    #     {
    #         'HTMLDocumentation': '{{children|first}}',
    #         'HTMLGUI': '{{children|first}}',
    #         'RoL': '{{children|first}}',
    #     },
    #     'localisation':
    #     {
    #         'pt': 'repetir'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'events': {
    #     'localisation':
    #     {
    #         'pt': 'eventos'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'Event': {
    #     'localisation':
    #     {
    #         'pt': 'eventos'
    #     },
    #     'documentation':
    #     {
    #     }
    # },
    #
    # 'Time': {
    #     'localisation':
    #     {
    #         'pt': 'eventos'
    #     },
    #     'documentation':
    #     {
    #     }
    # },

    # 'if': {
    #     'localisation':
    #     {
    #         'pt': 'se',
    #     },
    #     'documentation':
    #     {
    #     }
    # },
}
