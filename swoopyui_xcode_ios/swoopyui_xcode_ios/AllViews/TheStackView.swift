//
//  TheStackView.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 21/05/2023.
//

import SwiftUI

struct TheStackView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        if textData.stack_type?.lowercased() == "h" {
            HStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
                .onAppear() {
                    TellHostThisIsAppeared()
                }
            }
        }else if textData.stack_type?.lowercased() == "v" {
            VStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
                .onAppear() {
                    TellHostThisIsAppeared()
                }
            }
        }else if textData.stack_type?.lowercased() == "z" {
            ZStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
                .onAppear() {
                    TellHostThisIsAppeared()
                }
            }
        }
    }
    private func TellHostThisIsAppeared () {
        ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
            "action_name" : "on_appear",
            "view_id" : textData.view_id
        ])
    }
}
