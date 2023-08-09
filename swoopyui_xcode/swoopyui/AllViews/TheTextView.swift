

import SwiftUI

struct TheTextView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        if textData.bold == true {
            Text("\(textData.text!)")
                .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
                .bold().font(.system(size: CGFloat(textData.size!)))
                .onHover {d in
                    ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                        "action_name" : "on_hover",
                        "view_id" : textData.view_id,
                        "hover_state" : "\(d)"
                    ])
                }
        }else {
            Text("\(textData.text!)")
                .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
                .font(.system(size: CGFloat(textData.size!)))
                .onHover {d in
                    ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                        "action_name" : "on_hover",
                        "view_id" : textData.view_id,
                        "hover_state" : "\(d)"
                    ])
                }
        }
    }
}
