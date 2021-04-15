#!C:\Users\Support\AppData\Local\Microsoft\WindowsApps\python3.8.exe

subjects = {
    'ip' : { 
            'name' : 'Introduction to programming', 
            'year' : 1,
            'ects' : 6 
    },
    'c1' : { 
            'name' : 'Calculus 1', 
            'year' : 1, 
            'ects' : 7 
    },
    'cu' : { 
            'name' : 'Computer usage', 
            'year' : 1, 
            'ects' : 5 
    },
    'dmt' : { 
            'name' : 'Digital and microprocessor technology', 
            'year' : 1, 
            'ects' : 6 
    },
    'db' : { 
            'name' : 'Databases', 
            'year' : 2, 
            'ects' : 6 
    },
    'c2' : { 
            'name' : 'Calculus 2', 
            'year' : 2, 
            'ects' : 3 
    },
    'dsa' : { 
            'name' : 'Data structures and alghoritms',
            'year' : 2,
            'ects' : 5 
    },
    'ca' : { 
            'name' : 'Computer architecture',
            'year' : 2,    
            'ects' : 6 
    },
    'isd' : { 
            'name' : 'Information systems design', 
            'year' : 3, 
            'ects' : 5 
    },
    'c3' : { 
            'name' : 'Calculus 3', 
            'year' : 3, 
            'ects' : 7 
    },
    'sa' : { 
            'name' : 'Server Architecture', 
            'year' : 3, 
            'ects' : 6 
    },
    'cds' : { 
            'name' : 'Computer and data security', 
            'year' : 3, 
            'ects' : 6 
    }
}

def get_subjects():
    return subjects

def check(data, key):
    try:
        return str(data[key])
    except:
        return "none"
