
import DeepSecurity
import SmartCheck
import CloudConformity
import sys, inspect


def DSClasses():
    DSClasses=""
    print("function _thus_deepsecurity_classes() {")
    print("_arguments  \"1: :( ", end='')
    for name, obj in inspect.getmembers(DeepSecurity):

        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print(name.lower() + " ", end='')
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    ClassFunctions += fname.lower() + " "
                    #print(fname)



    print(")\"")
    print("return")
    print("}")

def DSFunctions():
    DSClasses=""
    print("function _thus_completions_deepsecurity_functions() {")
    print("  case $line[2] in")
    #print("_arguments  \"1: :( ", end='')
    for name, obj in inspect.getmembers(DeepSecurity):
        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print("  " + name.lower() + " )")
            print("    _arguments \"2: :( ", end='')
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    print(fname.lower() + " ", end='')
                    ClassFunctions += fname.lower() + " "
                    #print(fname)
            print(")\"")
            print("    return")
            print("    ;;")

    print(" *)")
    print("    _thus_deepsecurity_classes")
    print("    ;;")
    print("  esac")
    print("}")

def SCFunctions():
    DSClasses=""
    print("function _thus_completions_smartcheck_functions() {")
    print("  case $line[2] in")
    #print("_arguments  \"1: :( ", end='')
    for name, obj in inspect.getmembers(SmartCheck):
        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print("  " + name.lower() + " )")
            print("    _arguments \"2: :( ", end='')
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    print(fname.lower() + " ", end='')
                    ClassFunctions += fname.lower() + " "
                    #print(fname)
            print(")\"")
            print("    return")
            print("    ;;")

    print(" *)")
    print("    _thus_smartcheck_classes")
    print("    ;;")
    print("  esac")
    print("}")
def CCFunctions():
    DSClasses=""
    print("function _thus_completions_cc_functions() {")
    print("  case $line[2] in")
    #print("_arguments  \"1: :( ", end='')
    for name, obj in inspect.getmembers(CloudConformity):
        if inspect.ismodule(obj):
            name,obj = inspect.getmembers((obj))[0]
        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print("  " + name.lower() + " )")
            print("    _arguments \"2: :( ", end='')
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    print(fname.lower() + " ", end='')
                    ClassFunctions += fname.lower() + " "
                    #print(fname)
            print(")\"")
            print("    return")
            print("    ;;")

    print(" *)")
    print("    _thus_cc_classes")
    print("    ;;")
    print("  esac")
    print("}")

def SCClasses():
    DSClasses=""
    print("function _thus_smartcheck_classes() {")
    print("    _arguments \"1: :(", end='')
    for name, obj in inspect.getmembers(SmartCheck):

        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print(name.lower() + " ", end='')
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    ClassFunctions += fname.lower() + " "
                    #print(fname)

    print(")\"")
    print("    return")
    print("}")

def CCClasses():
    DSClasses=""
    print("function _thus_cc_classes() {")
    print("    _arguments \"1: :(", end='')
    for name, obj in inspect.getmembers(CloudConformity):
        if inspect.ismodule(obj):
            name,obj = inspect.getmembers((obj))[0]
        if inspect.isclass(obj) and not name.startswith("_") and name.lower() != "config" and name.lower() != "connection":
            DSClasses += name.lower() + " "
            ClassFunctions=""
            print(name.lower() + " ", end='')
            for fname, fobj in inspect.getmembers(obj):
                if (inspect.isfunction(fobj) or inspect.ismethod(fobj)) and not fname.startswith("_"):
                    #ClassFunctions.append(fname)
                    ClassFunctions += fname.lower() + " "
                    #print(fname)

    print(")\"")
    print("    return")
    print("}")

def CompleterMain():
    print("#compdef _thus thus")
    print("function _thus(){")
    print("    local line")
    print("    _arguments -C \\")
    print("        \"1: :(deepsecurity ds smartcheck sc workloadsecurity ws containersecurity cs)\" \\")
    print("        \"*::arg:->args\"")
    print("    case $line[1] in")
    print("        smartcheck | sc | cs | containersecurity)")
    print("            if [[ -z $line[2] ]]; then")
    print("              _thus_smartcheck_classes")
    print("            else")
    print("              _thus_completions_smartcheck_functions")
    print("            fi")
    print("        ;;")
    print("        deepsecurity | ds | ws | workloadsecurity)")
    print("         if [[ -z $line[2] ]]; then")
    print("            _thus_deepsecurity_classes")
    print("          else")
    print("              _thus_completions_deepsecurity_functions")
    print("            fi")
    print("        ;;")
    print("        cloudconformity | cc )")
    print("            if [[ -z $line[2] ]]; then")
    print("              _thus_cc_classes")
    print("            else")
    print("              _thus_completions_cc_functions")
    print("            fi")
    print("        ;;")
    print("    esac")
    print("}")

if __name__ == "__main__":

    #print("#compdef andi")
    CompleterMain()
    DSClasses()
    DSFunctions()
    SCFunctions()
    SCClasses()
    CCClasses()
    CCFunctions()