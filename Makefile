.PHONY: usage install run clean
  
.DEFAULT: usage
usage:
	@echo "make install : install required dependencies."
	@echo "make run : run the bot."
	@echo "make clean : remove bytecode and datafiles (logs & temporary files.)"
  
install:
	python3 -m pip install -U discord.py --user
	python3 -m pip install -U psutil --user
	mkdir -p keys
	chmod 755 startup
  
run:
	python GoodBot/goodbot.py
  
clean:
	# This intentionally fails when keys haven't been cleaned-up.
	rmdir keys
