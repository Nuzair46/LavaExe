from os import system, popen

class Start():
	def update():
		print("[INFO] Removing existing Lavalink (If any).")
		system("rm Lavalink.jar")
		try:
			system("curl -L https://github.com/freyacodes/Lavalink/releases/latest/download/Lavalink.jar -O")
			print("[INFO] Update complete...")
			Start.run()
		except Exception as e:
			print("[INFO] Latest version has no archive.")

	def run():
		print("[INFO] Starting Lavalink...")
		try:
			system("java -jar Lavalink.jar")
		except Exception as e:
			print("[ERROR] Error starting Lavalink.")

if __name__ == '__main__':
	Start.update()