

import SwiftUI

struct TheTextView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        if textData.bold == true {
            Text("\(textData.text!)")
                .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
                .bold().font(.system(size: CGFloat(textData.size!)))
        }else {
            Text("\(textData.text!)")
                .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
                .font(.system(size: CGFloat(textData.size!)))
        }
    }
}
