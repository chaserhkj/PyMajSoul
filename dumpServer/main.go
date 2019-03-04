package main

import (
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strconv"

	"github.com/gorilla/mux"
)

var addr = flag.String("addr", ":4433", "http service address")
var cert = flag.String("cert", "./cert.pem", "TLS certificate")
var priv = flag.String("priv", "./key.pem", "TLS private key")
var root = flag.String("root", "./", "Root directory to dump into")
var nameOnly = flag.String("nameOnly", "", "Set to enable recording name only to the specific file")
var file *os.File

func rootHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	w.Write([]byte("dumpServer standby"))
}

func getHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	path := mux.Vars(req)["path"]
	if _, err := os.Stat(filepath.Join(*root, path)); os.IsNotExist(err) {
		w.Write([]byte("false"))
	} else {
		w.Write([]byte("true"))
	}
}

func postHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	path := mux.Vars(req)["path"]
	path = filepath.Join(*root, path)
	file, err := os.Create(path)
	if err != nil {
		return
	}
	n, err := io.Copy(file, req.Body)
	if err != nil {
		return
	}
	w.Write([]byte(strconv.FormatInt(n, 10)))
}

func nameOnlyHandler(w http.ResponseWriter, req *http.Request) {
	w.Header().Set("Content-Type", "text/plain")
	w.Header().Set("Access-Control-Allow-Origin", "*")
	path := mux.Vars(req)["path"]
	fmt.Fprintln(file, path)
}

func main() {
	flag.Parse()

	r := mux.NewRouter()
	r.HandleFunc("/", rootHandler)
	if *nameOnly == "" {
		r.HandleFunc("/{path}", getHandler).Methods("GET")
		r.HandleFunc("/{path}", postHandler).Methods("POST")
	} else {
		var err error
		file, err = os.Create(*nameOnly)
		if err != nil {
			log.Fatal("Creating file: ", err)
		}
		r.HandleFunc("/{path}", nameOnlyHandler)
	}
	http.Handle("/", r)

	err := http.ListenAndServeTLS(*addr, *cert, *priv, nil)
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}
}
