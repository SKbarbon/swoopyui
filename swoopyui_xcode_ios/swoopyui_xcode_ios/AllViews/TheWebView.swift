import WebViewKit
import SwiftUI

struct TheWebView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        if textData.resizeable == true {
            WebView(url: URL(string: "\(textData.value!)")!)
                .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
        }else{
            WebView(url: URL(string: "\(textData.value!)")!)
        }
    }
}
