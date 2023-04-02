package main

import (

	"fmt"	"os/exec"

	"strings"

	"math/rand"

	"time"

)

const (

	sshDir   = "/home/user/.ssh"

	sshKey   = "id_rsa"

	firewall = "iptables"

)

func main() {

	if err := createUser(); err != nil {

		fmt.Printf("Error creating user: %v\n", err)

		return

	}

	if err := setupSSHKey(); err != nil {

		fmt.Printf("Error setting up SSH key: %v\n", err)

		return

	}

	if err := installFirewall(); err != nil {

		fmt.Printf("Error installing firewall: %v\n", err)

		return

	}

	fmt.Println("Performing network scan...")

	go networkScan()

	fmt.Println("All tasks completed successfully")

}

func createUser() error {

	password := generatePassword()

	return exec.Command("useradd", "-m", "-s", "/bin/bash", "-p", password, "user").Run()

}

func setupSSHKey() error {

	if err := exec.Command("mkdir", "-p", sshDir).Run(); err != nil {

		return err

	}

	if err := exec.Command("ssh-keygen", "-t", "rsa", "-b", "4096", "-f", fmt.Sprintf("%s/%s", sshDir, sshKey), "-N", "").Run(); err != nil {

		return err

	}

	publicKey, err := exec.Command("cat", fmt.Sprintf("%s/%s.pub", sshDir, sshKey)).Output()

	if err != nil {

		return err

	}

	chmodCommand := fmt.Sprintf("chown -R user:user %s; chmod 700 %s; chmod 600 %s/%s %s/%s.pub; echo \"%s\" >> %s/authorized_keys", sshDir, sshDir, sshDir, sshKey, sshDir, sshKey, string(publicKey), sshDir)

	return exec.Command("sh", "-c", chmodCommand).Run()

}

func installFirewall() error {

	return exec.Command("apt-get", "-y", "install", firewall).Run()

}

func networkScan() {

	output, err := exec.Command("nmap", "localhost").Output()

	if err != nil {

		fmt.Printf("Error performing network scan: %v\n", err)

		return

	}

	fmt.Println(string(output))

}

func generatePassword() string {

	rand.Seed(time.Now().UnixNano())

	const chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

	var password strings.Builder

	for i := 0; i < 12; i++ {

		password.WriteByte(chars[rand.Intn(len(chars))])

	}

	return password.String()

}
