#!/usr/bin/python3 -u
import os, sys, subprocess
import time

__config_file = '/manifests/cluster.yml'
__config_kubeconfig = '/root/.kube/config'
__config_manifests = '/manifests/init.yml'

def help(exitcode=0):
    print("routines.py - control cluster bootstraping and destroying")
    print("")
    print("Usage:")
    print("  create - bootstraps cluster")
    print("  delete - destroys cluster")
    sys.exit(exitcode)

def create():
    # Wipe kubeconfig
    with open(__config_kubeconfig, 'w') as fd:
        fd.write('')

    # Create cluster
    proc = subprocess.Popen([
        "/usr/local/bin/kind",
        "create",
        "cluster",
        "--config",
        __config_file
    ], stdout=sys.stdout, stderr=sys.stderr, universal_newlines=True)
    proc.communicate()

    # Refactor kubeconfig
    for pattern in ['.clusters[0].cluster.server = "https://kubernetes:6443"']: # '.clusters[0].cluster."insecure-skip-tls-verify" = true'
        proc = subprocess.Popen([
            "/usr/bin/yq",
            "-i",
            "-y",
            pattern,
            __config_kubeconfig,
        ], stdout=sys.stdout, stderr=sys.stderr, universal_newlines=True)
        proc.communicate()

    time.sleep(5)

    # Owerride dns config for nodes
    proc = subprocess.Popen([
        "/usr/local/bin/docker",
        "exec",
        "-i",
        "kind-control-plane",
        "sh",
        "-c",
        "echo nameserver 10.254.254.254 > /etc/resolv.conf",
    ], stdout=sys.stdout, stderr=sys.stderr, universal_newlines=True)
    proc.communicate()

    # Apply few manifests
    proc = subprocess.Popen([
        "/usr/local/bin/kubectl",
        "create",
        "-f",
        __config_manifests,
    ], stdout=sys.stdout, stderr=sys.stderr, universal_newlines=True)
    proc.communicate()

def delete():
    # Delete cluster
    proc = subprocess.Popen([
        "/usr/local/bin/kind",
        "delete",
        "cluster",
    ], stdout=sys.stdout, stderr=sys.stderr, universal_newlines=True)
    proc.communicate()

def main():
    if len(sys.argv) != 2:
        help(exitcode=2)

    if sys.argv[1] == "create":
        create()
    elif sys.argv[1] == "delete":
        delete()
    elif sys.argv[1] == "help":
        help()
    else:
        print("bad command")
        help(exitcode=3)

if __name__ == "__main__":
    main()
