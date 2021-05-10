from os import system, popen

class Start():
	def update():
		print("[INFO] Removing existing Lavalink (If any).")
		system("rm Lavalink.jar")
		x = int(input("[1] - Master Build\n[2] - Dev Build\n: "))
		try:
			if x == 1:
				system("curl -L https://github.com/freyacodes/Lavalink/releases/latest/download/Lavalink.jar -O")
			elif x == 2:
				system("curl -L https://ci.fredboat.com/guestAuth/repository/download/Lavalink_Build/8845:id/Lavalink.jar -O")
			else:
				print("invalid choice.")
				exit()
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