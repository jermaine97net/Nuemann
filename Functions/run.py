import subprocess

# Run code lines 1
result = subprocess.run(['python', 'text.py'], stdout=subprocess.PIPE, text=True)

# Print the output
print(result.stdout)

# Print the return code
print(f'Return Code: {result.returncode}')

# # process_1=subprocess.run(['python', 'file.py', 'gen_forecasts'],stdout=subprocess.PIPE, text=True)
# process_2=subprocess.run(['python', 'forecast.py', 'distribution','None'],stdout=subprocess.PIPE, text=True)
# print(process_2.stdout)

