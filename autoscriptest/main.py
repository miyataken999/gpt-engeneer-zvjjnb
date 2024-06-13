from autoscriptest.config import Config
from autoscriptest.script_executor import ScriptExecutor
from autoscriptest.script_parser import ScriptParser

def main():
    config = Config("scripts", "output")
    script_executor = ScriptExecutor(config)
    script_parser = ScriptParser(config)
    script_file = "test_script.txt"
    script = script_parser.parse_script(script_file)
    script_executor.execute_script(script)

if __name__ == "__main__":
    main()