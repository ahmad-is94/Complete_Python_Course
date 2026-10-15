
exceptions = [ZeroDivisionError(), FileNotFoundError(), NameError()]

n_zd_errors = n_fnf_errors = n_name_errors = 0

try:
    for e in exceptions:
        raise e
except ZeroDivisionError:
    n_zd_errors += 1
except FileNotFoundError:
    n_fnf_errors += 1
except NameError:
    n_name_errors += 1
finally:
    print(f"ZeroDivisionError occurred {n_zd_errors} times.")
    print(f"FileNotFoundError occurred {n_fnf_errors} times.")
    print(f"NameError occurred {n_name_errors} times.")
