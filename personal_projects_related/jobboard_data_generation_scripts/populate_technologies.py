from faker import Faker
import sys


language_names = [
    "A.NET",
    "Ada",
    "Assembly language",
    "BASIC",
    "C",
    "C--",
    "C++",
    "C*",
    "C#",
    "Clojure",
    "COBOL",
    "D",
    "Dart",
    "Elixir",
    "Elm",
    "Emacs Lisp",
    "Emerald",
    "Epigram",
    "EPL",
    "Erlang",
    "Euclid",
    "Euler",
    "F",
    "F#",
    "F*",
    "Factor",
    "@Formula",
    "Forth",
    "Fortran",
    "Fortress",
    "FP",
    "Geometric Description Language",
    "GEORGE",
    "OpenGL Shading Language",
    "GNU E",
    "GNU Ubiquitous Intelligent Language for Extensions",
    "Go",
    "Go!",
    "Golo",
    "Good Old Mad",
    "Google Apps Script",
    "Gosu",
    "GOTRAN",
    "General Purpose Simulation System",
    "Harbour",
    "Hartmann pipelines",
    "Haskell",
    "Hermes",
    "High Level Assembly",
    "High Level Shader Language",
    "Hollywood",
    "HolyC",
    "Hop",
    "Hopscotch",
    "Hope",
    "Hume",
    "HyperTalk",
    "Hy",
    "I",
    "Io",
    "Icon",
    "Idris",
    "Inform",
    "ISLISP",
    "J",
    "J#",
    "J++",
    "JADE",
    "Jai",
    "JAL",
    "Janus",
    "Janus",
    "JASS",
    "Java",
    "JavaFX Script",
    "JavaScript",
    "Julia",
    "Jython",
    "K",
    "Kaleidoscope",
    "Karel",
    "KEE",
    "Kixtart",
    "Klerer-May System",
    "KIF",
    "Kojo",
    "Kotlin",
    "Kv",
    "Lasso",
    "LINQ",
    "LIS",
    "LISA",
    "Language H",
    "Lisp",
    "Lite-C",
    "Lithe",
    "Little b",
    "LLL",
    "Logo",
    "Logtalk",
    "Lua",
    "Lucid",
    "Lustre",
    "Lynx",
    "M#",
    "Machine code",
    "MAD",
    "MAD/I",
    "N",
    "NASM",
    "Nial",
    "Nickle",
    "Nim",
    "Nix",
    "NPL",
    "Not eXactly C",
    "Not Quite C",
    "Oz",
    "Pascal",
    "Pascal Script",
    "PCASTL",
    "PCF",
    "PEARL",
    "PeopleCode",
    "Perl",
    "PDL",
    "Pharo",
    "PHP",
    "Pico",
    "Picolisp",
    "Pict",
    "Pike",
    "PL/P",
    "PL/S",
    "PL/SQL",
    "PowerShell",
    "PPL",
    "Processing",
    "Processing.js",
    "Prograph",
    "Project Verona",
    "Prolog",
    "PROMAL",
    "PROTEL",
    "ProvideX",
    "Pro*C",
    "Pure",
    "Pure Data",
    "PureScript",
    "PWCT",
    "Python",
    "Q",
    "Q#",
    "QtScript",
    "QuakeC",
    "QPL",
    ".QL",
    "R",
    "R++",
    "RPG",
    "RPL",
    "RSL",
    "RTL/2",
    "Ruby",
    "Rust",
    "S",
    "S-Lang",
    "S-PLUS",
    "SA-C",
    "SabreTalk",
    "Scala",
    "Simula",
    "Simulink",
    "SISAL",
    "SKILL",
    "SLIP",
    "SMALL",
    "Smalltalk",
    "Superplan",
    "SuperTalk",
    "Swift",
    "Swift",
    "SYMPL",
    "T",
    "TeX",
    "TEX",
    "TypeScript",
    "U",
    "UNITY",
    "UnrealScript",
    "Viper",
    "Visual DataFlex",
    "Visual DialogScript",
    "Visual FoxPro",
    "Visual J++",
    "Visual LISP",
    "Visual Objects",
    "Visual Prolog",
    "W",
    "WATFIV",
    "WebAssembly",
    "Wyvern",
    "X",
    "X++",
    "X10",
    "xBase++",
    "XSB",
    "XSharp",
    "XSLT",
    "Xtend",
    "Y",
    "Yorick",
    "YQL",
    "Yoix",
    "Z",
    "Zig",
    "Zonnon",
    "ZOPL",
    "ZPL",
    "Z++",
]


fake = Faker()

def get_tech_name():
    return fake.random_element(language_names)


def get_desc():
    return fake.sentence(nb_words=25)

def assemble_queries(amount):
    queries = []
    for i in range(amount):
        query = "INSERT INTO technology (name, description) VALUES ('" + \
            get_tech_name() + "', '" + get_desc() + "');"
        queries.append(query)

    return queries


def write_queries_to_file(queries):
    with open('populate_technologies.sql', 'w') as file:
        for query in queries:
            file.write(query + "\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python populate_technologies.py <amount_of_technologies>")
        return

    amount = int(sys.argv[1])

    queries = assemble_queries(amount)

    write_queries_to_file(queries)


if __name__ == "__main__":
    main()
