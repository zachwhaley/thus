
import DeepSecurity
import SmartCheck
import CloudConformity
import sys, inspect

services = [
        'DeepSecurity',
        "smartcheck"
]

def CCFunctions():
    DSClasses = ""
    print("_thus_completions_cc_functions()")
    print("{")

    print("case \"${COMP_WORDS[COMP_CWORD-1]}\" in ")
    for name, obj in inspect.getmembers(CloudConformity):
        if inspect.ismodule(obj):
            name,obj = inspect.getmembers((obj))[0]
        t = inspect.isclass(obj)
        if inspect.isclass(obj) and not name.startswith(
                "_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions = ""
            print("\t" + name.lower() + ")")
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    # ClassFunctions.append(fname)
                    ClassFunctions += fname.lower() + " "
                    # print(fname)

            print("\t\t COMPREPLY=($(compgen -W \"" + ClassFunctions + "\" \"${COMP_WORDS[3]}\"))")
            print("\t\t return")
            print("\t\t;;")
    print("esac")
    print("}")
    print("_thus_completions_cc_classes()")
    print("{")
    print("COMPREPLY=($(compgen -W \"" + DSClasses + "\" \"${COMP_WORDS[2]}\"))")
    print("return")
    print("}")

def DSFunctions():
    DSClasses=""
    print("_thus_completions_ds_functions()")
    print("{")

    print("case \"${COMP_WORDS[COMP_CWORD-1]}\" in ")
    for name, obj in inspect.getmembers(DeepSecurity):

        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print("\t" + name.lower() + ")")
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    ClassFunctions += fname.lower() + " "
                    #print(fname)

            print("\t\t COMPREPLY=($(compgen -W \"" + ClassFunctions +"\" \"${COMP_WORDS[3]}\"))")
            print("\t\t return")
            print("\t\t;;")
    print("esac")
    print("}")
    print("_thus_completions_ds_classes()")
    print("{")
    print("COMPREPLY=($(compgen -W \"" + DSClasses +"\" \"${COMP_WORDS[2]}\"))")
    print("return")
    print("}")
def SCFunctions():
    DSClasses=""
    print("_thus_completions_cs_functions()")
    print("{")

    print("case \"${COMP_WORDS[COMP_CWORD-1]}\" in ")
    for name, obj in inspect.getmembers(SmartCheck):

        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print("\t" + name.lower() + ")")
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    ClassFunctions += fname.lower() + " "
                    #print(fname)

            print("\t\t COMPREPLY=($(compgen -W \"" + ClassFunctions +"\" \"${COMP_WORDS[3]}\"))")
            print("\t\t return")
            print("\t\t;;")
    print("esac")
    print("}")
    print("_thus_completions_cs_classes()")
    print("{")
    print("COMPREPLY=($(compgen -W \"" + DSClasses +"\" \"${COMP_WORDS[2]}\"))")
    print("return")
    print("}")

def BuildMainFunction():
    print("_thus_completions()")
    print("{")
    print("  local cloudone_services=\"deepsecurity ds smartcheck sc workloadsecurity ws containersecurity cs cc cloudconformity\" ")
    print("  COMPREPLY=()")
    print("  if [ \"${#COMP_WORDS[@]}\" == \"2\" ]; then")
    print("    COMPREPLY=($(compgen -W \"${cloudone_services}\" \"${COMP_WORDS[1]}\")) ")
    print("    return")
    print("  fi")
    print("  service=${COMP_WORDS[1]}")
    print("  case ${service} in ")
    print("    workloadsecurity | ws | ds) ")
    print("        service=\"deepsecurity\" ")
    print("       ;; ")
    print("    containersecurity | cs | sc) ")
    print("        service=\"smartcheck\" ")
    print("        ;;")
    print("    cloudconformity | cc) ")
    print("        service=\"cloudconformity\" ")
    print("        ;;")
    print("    esac")
    print("  if [ \"${#COMP_WORDS[@]}\" == \"3\" ]; then")
    print("    case ${service} in")
    print("         deepsecurity)")
    print("              _thus_completions_ds_classes")
    print("              return")
    print("         ;;")
    print("         smartcheck)")
    print("             _thus_completions_cs_classes")
    print("             return")
    print("         ;;")
    print("         cloudconformity)")
    print("             _thus_completions_cc_classes")
    print("             return")
    print("         ;;")
    print("     esac")
    print("     return")
    print("   fi")
    print("    if [ \"${#COMP_WORDS[@]}\" == \"4\" ]; then")
    print("    case ${service} in")
    print("        deepsecurity)")
    print("            _thus_completions_ds_functions")
    print("            return")
    print("        ;;")
    print("        smartcheck)")
    print("            _thus_completions_cs_functions")
    print("            return")
    print("        ;;")
    print("        cloudconformity)")
    print("            _thus_completions_cc_functions")
    print("            return")
    print("        ;;")
    print("    esac")
    print("    return")
    print("  fi")
    print("}")
    print("complete -F _thus_completions thus")

if __name__ == "__main__":

    print("#/usr/bin/env bash")
    CCFunctions()
    DSFunctions()
    SCFunctions()
    BuildMainFunction()
