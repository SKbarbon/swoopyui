import Foundation

func submit_and_run_python_target_function (host_port:String){
        let url = URL(string: "http://127.0.0.1:\(host_port)/start_the_target_function")!

        let task = URLSession.shared.dataTask(with: url) { data, response, error in
            if let data = data {
                _ = String(data: data, encoding: String.Encoding.utf8) as String?
            } else if let error = error {
                print("HTTP Request Failed \(error)")
            }
        }

        task.resume()
    }
