//
//  TheNavigationStack.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 19/05/2023.
//

import SwiftUI

struct TheNavigationStack: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        NavigationStack {
            VStack {
                ForEach(textData.sub_views!, id: \.view_id) { sub_view in
                    GetTheDataView(swoopyuiViewData: sub_view, hostPort: host_port)
                }
            }
            .navigationTitle("\(textData.title!)")
        }
        .onAppear {
            ClientSideUpdateReq(hostPort: host_port, update_name: "on_view_action", update_content: [
                "action_name" : "on_appear",
                "view_id" : textData.view_id
            ])
        }
    }
}
