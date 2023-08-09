//
//  TheTextField.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 19/05/2023.
//

import SwiftUI

struct TheTextField: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    
    @State var input = ""
    var body: some View {
        TextField("\(textData.placeholder!)", text: $input)
            .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
            .frame(width: CGFloat(textData.width!), height: CGFloat(textData.height!))
            .onChange(of: input, perform:{value in
                ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                    "action_name" : "on_change",
                    "text" : input,
                    "view_id" : textData.view_id
                ])
        })
            .onSubmit {
                ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                    "action_name" : "on_submit",
                    "text" : input,
                    "view_id" : textData.view_id
            ])
        }
            .onAppear() {
                input = textData.text ?? ""
            }
    }
}
